# Generated from grammar/matlab.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .matlabParser import matlabParser
else:
    from matlabParser import matlabParser

# This class defines a complete generic visitor for a parse tree produced by matlabParser.

class matlabVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by matlabParser#programa.
    def visitPrograma(self, ctx:matlabParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#instrucao.
    def visitInstrucao(self, ctx:matlabParser.InstrucaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#instrucaoSimples.
    def visitInstrucaoSimples(self, ctx:matlabParser.InstrucaoSimplesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#blocoDeInstrucoes.
    def visitBlocoDeInstrucoes(self, ctx:matlabParser.BlocoDeInstrucoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#instrucaoDeBloco.
    def visitInstrucaoDeBloco(self, ctx:matlabParser.InstrucaoDeBlocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#instrucaoIf.
    def visitInstrucaoIf(self, ctx:matlabParser.InstrucaoIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#instrucaoFor.
    def visitInstrucaoFor(self, ctx:matlabParser.InstrucaoForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#instrucaoWhile.
    def visitInstrucaoWhile(self, ctx:matlabParser.InstrucaoWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#ladoEsquerdoAtribuicao.
    def visitLadoEsquerdoAtribuicao(self, ctx:matlabParser.LadoEsquerdoAtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#atribuicao.
    def visitAtribuicao(self, ctx:matlabParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#expressao.
    def visitExpressao(self, ctx:matlabParser.ExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#expressaoOuLogico.
    def visitExpressaoOuLogico(self, ctx:matlabParser.ExpressaoOuLogicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#expressaoELogico.
    def visitExpressaoELogico(self, ctx:matlabParser.ExpressaoELogicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#expressaoComparacao.
    def visitExpressaoComparacao(self, ctx:matlabParser.ExpressaoComparacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#expressaoIntervalo.
    def visitExpressaoIntervalo(self, ctx:matlabParser.ExpressaoIntervaloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#expressaoAditiva.
    def visitExpressaoAditiva(self, ctx:matlabParser.ExpressaoAditivaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#expressaoMultiplicativa.
    def visitExpressaoMultiplicativa(self, ctx:matlabParser.ExpressaoMultiplicativaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#expressaoPotencia.
    def visitExpressaoPotencia(self, ctx:matlabParser.ExpressaoPotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#expressaoUnaria.
    def visitExpressaoUnaria(self, ctx:matlabParser.ExpressaoUnariaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#atomo.
    def visitAtomo(self, ctx:matlabParser.AtomoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#listaArgumentos.
    def visitListaArgumentos(self, ctx:matlabParser.ListaArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#matriz.
    def visitMatriz(self, ctx:matlabParser.MatrizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#linhasMatriz.
    def visitLinhasMatriz(self, ctx:matlabParser.LinhasMatrizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by matlabParser#linha.
    def visitLinha(self, ctx:matlabParser.LinhaContext):
        return self.visitChildren(ctx)



del matlabParser