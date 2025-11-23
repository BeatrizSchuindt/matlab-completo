from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Any


class ASTNode:
    """
    Nó base da AST. Todos os outros nós herdam desta classe.
    """
    def accept(self, visitor: Any):
        """
        Implementa o padrão Visitor.
        O visitor deve ter um método do tipo visit_NomeDaClasse.
        Ex: para ProgramNode -> visit_ProgramNode
        """
        method_name = "visit_" + self.__class__.__name__
        visit = getattr(visitor, method_name, None)
        if visit is None:
            raise NotImplementedError(
                f"{visitor.__class__.__name__} não implementa {method_name}"
            )
        return visit(self)


# ==========================
# NÓS DE PROGRAMA / BLOCO
# ==========================
@dataclass
class ProgramNode(ASTNode):
    """
    programa: PROGRAMA ID bloco ;
    """
    name: str                      # ID do programa
    block: BlockNode               # corpo principal


@dataclass
class BlockNode(ASTNode):
    """
    bloco: LCHAVE (declaracao)* (comando)* RCHAVE ;
    """
    declarations: List[DeclarationNode] = field(default_factory=list)
    commands: List[CommandNode] = field(default_factory=list)


# ==========================
# DECLARAÇÕES E VARIÁVEIS
# ==========================
@dataclass
class DeclarationNode(ASTNode):
    """
    declaracao: tipo varinicial (VIRGULA varinicial)* PV ;
    """
    type_name: str                      # "int", "real", "texto" etc.
    var_inits: List[VarInitNode]        # lista de variáveis declaradas


@dataclass
class VarInitNode(ASTNode):
    """
    varinicial: ID (ATRIBUI expressao)? ;
    """
    name: str                           # nome da variável
    initial_value: Optional[ExpressionNode] = None  # expressão de inicialização (se existir)


# ==========================
# TIPOS
# ==========================
@dataclass
class TypeNode(ASTNode):
    """
    Wrapper opcional para tipo.
    tipo: INT | REAL | TEXTO ;
    """
    name: str                           # "int", "real", "texto"


# ==========================
# COMANDOS (BASE)
# ==========================
class CommandNode(ASTNode):
    """
    Nó base para qualquer comando.
    comando:
        escrita
      | leitura
      | atribuicao
      | enquanto
      | repita
      | laco_para
      | loop_infinito
      | incremento PV
      ;
    """
    pass


# ==========================
# COMANDOS ESPECÍFICOS
# ==========================
@dataclass
class WriteNode(CommandNode):
    """
    escrita: ESCREVA (expressao | STRING) PV ;
    """
    expression: Optional[ExpressionNode] = None
    string_value: Optional[str] = None   # quando for ESCREVA "texto literal"


@dataclass
class ReadNode(CommandNode):
    """
    leitura: LER ID PV ;
    """
    var_name: str


@dataclass
class AssignNode(CommandNode):
    """
    atribuicao: ID ATRIBUI expressao PV ;
    (supondo essa forma no seu grammar)
    """
    target: IdentifierNode
    value: ExpressionNode


@dataclass
class WhileNode(CommandNode):
    """
    enquanto: ENQUANTO expressao bloco ;
    (ajuste conforme sua gramática real)
    """
    condition: ExpressionNode
    body: BlockNode


@dataclass
class RepeatNode(CommandNode):
    """
    repita: REPITA bloco ATE expressao PV ;
    """
    body: BlockNode
    condition: ExpressionNode


@dataclass
class ForNode(CommandNode):
    """
    laco_para: PARA ID DE expressao ATE expressao (PASSO expressao)? bloco ;
    (exemplo genérico)
    """
    var_name: str
    start: ExpressionNode
    end: ExpressionNode
    step: Optional[ExpressionNode]
    body: BlockNode


@dataclass
class InfiniteLoopNode(CommandNode):
    """
    loop_infinito: LOOP bloco ;
    (exemplo genérico para 'loop_infinito')
    """
    body: BlockNode


@dataclass
class IncrementNode(CommandNode):
    """
    incremento: ID OP_INC ;
    ou algo parecido (++, --, etc.)
    """
    var_name: str
    op: str = "++"        # ou "--", etc.


# ==========================
# EXPRESSÕES
# ==========================
class ExpressionNode(ASTNode):
    """
    Nó base para expressões.
    expressao: termo (OP_ADD termo)* ;
    termo: ... ;
    """
    pass


@dataclass
class BinaryOpNode(ExpressionNode):
    """
    Nó para operações binárias (a OP b).
    Ex: +, -, *, /, <, >, ==, etc.
    """
    left: ExpressionNode
    op: str
    right: ExpressionNode


@dataclass
class UnaryOpNode(ExpressionNode):
    """
    Operações unárias, ex: -a, +a, !a
    """
    op: str
    operand: ExpressionNode


@dataclass
class LiteralNode(ExpressionNode):
    """
    Literais numéricos ou de texto.
    Ex: 10, 3.14, "teste"
    """
    value: Any


@dataclass
class IdentifierNode(ExpressionNode):
    """
    Usado para referenciar variáveis.
    """
    name: str
