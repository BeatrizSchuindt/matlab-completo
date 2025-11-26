from typing import List, Optional
import re

from src.gen.grammar.matlabParser import matlabParser
from src.gen.grammar.matlabVisitor import matlabVisitor


class MatlabCodeGenVisitor(matlabVisitor):
    """
    Visitor responsável por percorrer a AST de Matlab-like
    e gerar código Python equivalente.

    Uso típico (após passar pela análise semântica):

        visitor = MatlabCodeGenVisitor(output_file="output.py")
        visitor.visit(tree)
    """

    def __init__(self, output_file: Optional[str] = None) -> None:
        super().__init__()
        self.output_lines: List[str] = []
        self.indent_level: int = 0
        self.output_file: Optional[str] = output_file

        self.builtin_functions = {"input", "fprintf", "error", "zeros"}

    def _indent(self) -> str:
        return "    " * self.indent_level

    def emit(self, line: str = "") -> None:
        """Adiciona uma linha ao código de saída, já indentada."""
        if line:
            self.output_lines.append(self._indent() + line)
        else:
            self.output_lines.append("")

    def increase_indent(self) -> None:
        self.indent_level += 1

    def decrease_indent(self) -> None:
        self.indent_level -= 1
        if self.indent_level < 0:
            self.indent_level = 0

    def get_code(self) -> str:
        return "\n".join(self.output_lines)

    def save(self) -> None:
        if self.output_file:
            with open(self.output_file, "w", encoding="utf-8") as f:
                f.write(self.get_code())

    def _emit_helpers(self) -> None:
        """
        Funções auxiliares emitidas no topo do arquivo Python gerado.
        Aqui tratamos, por exemplo, zeros() em estilo Matlab.
        """
        # zeros
        self.emit("def zeros(m, n=None):")
        self.increase_indent()
        self.emit('"""Aproximação simples de zeros do Matlab."""')
        self.emit("if n is None:")
        self.increase_indent()
        self.emit("return [0] * m")
        self.decrease_indent()
        self.emit("if m == 1:")
        self.increase_indent()
        self.emit("return [0] * n")
        self.decrease_indent()
        self.emit("if n == 1:")
        self.increase_indent()
        self.emit("return [0] * m")
        self.decrease_indent()
        self.emit("return [[0 for _ in range(n)] for _ in range(m)]")
        self.decrease_indent()
        self.emit("")

    # ----- helpers de indexação 1-based → 0-based -----

    def _index_expr(self, expr_code: str) -> str:
        expr_code = expr_code.strip()

        if re.fullmatch(r"\d+", expr_code):
            return str(int(expr_code) - 1)

        # caso geral: expr - 1
        return f"({expr_code} - 1)"

    def _rewrite_indexing(self, code: str) -> str:
        pattern = re.compile(r"([A-Za-z_]\w*)\(([^()]*)\)")

        def repl(match: re.Match) -> str:
            name = match.group(1)
            args_str = match.group(2).strip()

            if name in self.builtin_functions:
                return match.group(0)

            if not args_str:
                # algo como x() – trata como variável simples
                return name

            args = [a.strip() for a in args_str.split(",") if a.strip()]

            # converte cada argumento de 1-based para 0-based
            indices = [self._index_expr(a) for a in args]

            if len(indices) == 1:
                # v(i) -> v[i-1]
                return f"{name}[{indices[0]}]"

            # A(i, j) -> A[i-1][j-1]
            index_str = "".join(f"[{idx}]" for idx in indices)
            return f"{name}{index_str}"

        return pattern.sub(repl, code)

    def _translate_expression(self, ctx) -> str:
        text = ctx.getText()

        # Comparação diferente
        text = text.replace("~=", "!=")

        # Operadores lógicos
        text = text.replace("&&", " and ")
        text = text.replace("||", " or ")
        text = text.replace(".^", "**")
        text = text.replace("^", "**")
        text = text.replace(".*", "*")
        text = text.replace("./", "/")

        # Indexação Matlab 1-based: row(j) -> row[j-1], etc.
        text = self._rewrite_indexing(text)

        return text

    def _translate_for_expression(self, expr_text: str) -> str:
        """
        Traduz expressões de intervalo Matlab para range() em Python.

        Exemplos:
          "1:n"       -> "range(1, n + 1)"
          "1:2:10"    -> "range(1, 10 + 1, 2)"
        """
        parts = [p.strip() for p in expr_text.split(":")]
        if len(parts) == 1:
            return parts[0]
        if len(parts) == 2:
            start, end = parts
            return f"range({start}, {end} + 1)"
        if len(parts) == 3:
            start, step, end = parts
            return f"range({start}, {end} + 1, {step})"
        return expr_text

    def _translate_fprintf(self, code: str) -> str:
        """
        Aproximação de fprintf em Python usando print.
        Suporta principal caso: fprintf('%d', valor)
        e fprintf('\\n').
        """
        code = code.strip()
        if not code.startswith("fprintf(") or not code.endswith(")"):
            return code

        inner = code[len("fprintf("):-1].strip()
        if not inner:
            return "print()"

        parts = [p.strip() for p in inner.split(",", 1)]
        fmt = parts[0]
        if len(parts) == 1:
            return f"print({fmt}, end='')"

        args = parts[1]
        return f"print({fmt} % ({args}), end='')"

    def _translate_error(self, code: str) -> str:
        """Traduz error('msg') para raise Exception('msg')."""
        code = code.strip()
        if not code.startswith("error(") or not code.endswith(")"):
            return code
        inner = code[len("error("):-1].strip()
        if not inner:
            inner = "''"
        return f"raise Exception({inner})"

    def _rewrite_expression_for_assignment(self, code: str) -> str:
        """
        Reescreve a expressão do lado direito em atribuições
        para tratar alguns casos especiais (como input()).
        """
        stripped = code.strip()
        if stripped.startswith("input("):
            return f"int({stripped})"
        return code

    def _rewrite_expression_as_statement(self, code: str) -> str:
        """
        Reescreve expressões usadas como instruções (linhas soltas)
        para tratar fprintf, error, etc.
        """
        stripped = code.strip()
        if stripped.startswith("fprintf("):
            return self._translate_fprintf(stripped)
        if stripped.startswith("error("):
            return self._translate_error(stripped)
        return code

    # ========= Regras principais da gramática =========

    def visitPrograma(self, ctx: matlabParser.ProgramaContext):
        """
        programa: instrucao* EOF;
        """
        self.emit("# -*- coding: utf-8 -*-")
        self.emit("# Código Python gerado automaticamente a partir de Matlab-like")
        self.emit("")

        self._emit_helpers()

        for instr_ctx in ctx.instrucao():
            self.visit(instr_ctx)

        self.save()
        return None

    def visitInstrucao(self, ctx: matlabParser.InstrucaoContext):
        """
        instrucao
            : instrucaoDeBloco (SEMI | NEWLINE+)?
            | instrucaoSimples
            | NEWLINE+
            ;
        """
        if ctx.instrucaoDeBloco():
            self.visit(ctx.instrucaoDeBloco())
        elif ctx.instrucaoSimples():
            self.visit(ctx.instrucaoSimples())
        else:
            # Apenas quebras de linha – nada a gerar
            pass
        return None

    def visitInstrucaoSimples(self, ctx: matlabParser.InstrucaoSimplesContext):
        """
        instrucaoSimples
            : (atribuicao | expressao) (SEMI | NEWLINE+)
            ;
        """
        if ctx.atribuicao():
            assign_code = self.visit(ctx.atribuicao())
            if assign_code:
                self.emit(assign_code)
        elif ctx.expressao():
            expr_code = self.visit(ctx.expressao())
            if expr_code:
                expr_code = self._rewrite_expression_as_statement(expr_code)
                self.emit(expr_code)
        return None

    def visitBlocoDeInstrucoes(self, ctx: matlabParser.BlocoDeInstrucoesContext):
        """
        blocoDeInstrucoes: instrucao*;
        """
        for instr_ctx in ctx.instrucao():
            self.visit(instr_ctx)
        return None

    def visitInstrucaoDeBloco(self, ctx: matlabParser.InstrucaoDeBlocoContext):
        """
        instrucaoDeBloco
            : instrucaoIf
            | instrucaoFor
            | instrucaoWhile
            ;
        """
        if ctx.instrucaoIf():
            self.visit(ctx.instrucaoIf())
        elif ctx.instrucaoFor():
            self.visit(ctx.instrucaoFor())
        elif ctx.instrucaoWhile():
            self.visit(ctx.instrucaoWhile())
        return None

    # ========= Estruturas de controle =========

    def visitInstrucaoIf(self, ctx: matlabParser.InstrucaoIfContext):
        """
        instrucaoIf
            : KW_IF expressao blocoDeInstrucoes
              (KW_ELSEIF expressao blocoDeInstrucoes)*
              (KW_ELSE blocoDeInstrucoes)?
              KW_END
            ;
        """
        exprs = list(ctx.expressao())
        blocks = list(ctx.blocoDeInstrucoes())

        # if principal
        cond_if = self.visit(exprs[0])
        self.emit(f"if {cond_if}:")
        self.increase_indent()
        self.visit(blocks[0])
        self.decrease_indent()

        # elseif -> elif
        for i in range(1, len(exprs)):
            cond_elif = self.visit(exprs[i])
            self.emit(f"elif {cond_elif}:")
            self.increase_indent()
            self.visit(blocks[i])
            self.decrease_indent()

        # else (se existir)
        if len(blocks) > len(exprs):
            self.emit("else:")
            self.increase_indent()
            self.visit(blocks[-1])
            self.decrease_indent()

        return None

    def visitInstrucaoFor(self, ctx: matlabParser.InstrucaoForContext):
        """
        instrucaoFor
            : KW_FOR ID ASSIGN expressao blocoDeInstrucoes KW_END
            ;
        """
        var_name = ctx.ID().getText()
        expr_code = self.visit(ctx.expressao())
        iter_code = self._translate_for_expression(expr_code)

        self.emit(f"for {var_name} in {iter_code}:")
        self.increase_indent()
        self.visit(ctx.blocoDeInstrucoes())
        self.decrease_indent()
        return None

    def visitInstrucaoWhile(self, ctx: matlabParser.InstrucaoWhileContext):
        """
        instrucaoWhile
            : KW_WHILE expressao blocoDeInstrucoes KW_END
            ;
        """
        cond_code = self.visit(ctx.expressao())
        self.emit(f"while {cond_code}:")
        self.increase_indent()
        self.visit(ctx.blocoDeInstrucoes())
        self.decrease_indent()
        return None

    # ========= Atribuições e lado esquerdo =========

    def visitLadoEsquerdoAtribuicao(self, ctx: matlabParser.LadoEsquerdoAtribuicaoContext):
        """
        ladoEsquerdoAtribuicao
            : ID
            | ID LPAREN listaArgumentos? RPAREN
            ;
        """
        name = ctx.ID().getText()
        if ctx.LPAREN() is None:
            # Atribuição simples: x = ...
            return name

        indices: List[str] = []
        if ctx.listaArgumentos():
            for expr_ctx in ctx.listaArgumentos().expressao():
                raw_idx = self.visit(expr_ctx)          
                idx_code = self._index_expr(raw_idx)
                indices.append(idx_code)

        if not indices:
            return name

        if len(indices) == 1:
            return f"{name}[{indices[0]}]"
        else:
            # Versão simplificada: multi-dim como name[i][j]...
            index_str = "".join(f"[{idx}]" for idx in indices)
            return f"{name}{index_str}"

    def visitAtribuicao(self, ctx: matlabParser.AtribuicaoContext):
        """
        atribuicao
            : ladoEsquerdoAtribuicao ASSIGN expressao
            ;
        """
        left_code = self.visit(ctx.ladoEsquerdoAtribuicao())
        right_code = self.visit(ctx.expressao())
        right_code = self._rewrite_expression_for_assignment(right_code)
        return f"{left_code} = {right_code}"

    # ========= Expressões =========

    def visitExpressao(self, ctx: matlabParser.ExpressaoContext):
        """
        expressao
            : expressaoOuLogico
            ;
        """
        return self._translate_expression(ctx)
