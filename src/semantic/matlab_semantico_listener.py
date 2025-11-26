from antlr4 import *
from src.gen.grammar.matlabParser import matlabParser
from src.gen.grammar.matlabListener import matlabListener

from src.semantic.tabela_simbolos import Scope
from src.semantic.erros_semanticos import SemanticError


class MatlabSemanticListener(matlabListener):
    def __init__(self):
        super().__init__()
        # escopo global
        self.global_scope = Scope("global", None)
        self.current_scope = self.global_scope
        self.errors = []

        builtin_funcs = [
            "input",    # leitura do teclado
            "fprintf",  # impressão formatada
            "error",    # mensagem de erro
            "zeros",    # criação de vetor/matriz de zeros
            "disp",
            "ones",
            "eye",
        ]

        for name in builtin_funcs:
            # marca como função embutida no escopo global
            self.global_scope.define(name, type_="builtin_function")

    # ---------- utilitários internos ----------
    def push_scope(self, name):
        self.current_scope = Scope(name, self.current_scope)

    def pop_scope(self):
        if self.current_scope.parent is not None:
            self.current_scope = self.current_scope.parent

    def report_error(self, ctx, message):
        token = ctx.start  # todo ctx de regra tem .start
        line = token.line
        column = token.column
        self.errors.append(SemanticError(line, column, message))

    # ---------- gestão de escopos ----------
    def enterPrograma(self, ctx: matlabParser.ProgramaContext):
        self.current_scope = self.global_scope

    def enterBlocoDeInstrucoes(self, ctx: matlabParser.BlocoDeInstrucoesContext):
        # bloco de if/for/while entra em novo escopo
        self.push_scope("block")

    def exitBlocoDeInstrucoes(self, ctx: matlabParser.BlocoDeInstrucoesContext):
        # sai do escopo do bloco
        self.pop_scope()

    # ---------- definição de variáveis ----------
    def exitLadoEsquerdoAtribuicao(self, ctx: matlabParser.LadoEsquerdoAtribuicaoContext):
        """
        ladoEsquerdoAtribuicao
            : ID
            | ID LPAREN listaArgumentos? RPAREN
        """
        name = ctx.ID().getText()
        self.current_scope.define(name, type_="var")

    def enterInstrucaoFor(self, ctx: matlabParser.InstrucaoForContext):
        """
        instrucaoFor
            : KW_FOR ID ASSIGN expressao blocoDeInstrucoes KW_END
        """
        var_name = ctx.ID().getText()
        self.current_scope.define(var_name, type_="var")

    # ---------- uso de identificadores ----------
    def exitAtomo(self, ctx: matlabParser.AtomoContext):
        """
        atomo
            : LPAREN expressao RPAREN
            | matriz
            | ID LPAREN listaArgumentos? RPAREN
            | ID
            | NUMBER
            | STRING
        """
        # Se for NUMBER ou STRING, nada pra checar
        if ctx.NUMBER() or ctx.STRING():
            return

        # Uso de identificador (variável ou função)
        if ctx.ID():
            name = ctx.ID().getText()

            # Se não estiver definido em nenhum escopo -> erro semântico
            if self.current_scope.resolve(name) is None:
                self.report_error(
                    ctx,
                    f"Identificador '{name}' usado antes de ser definido."
                )


