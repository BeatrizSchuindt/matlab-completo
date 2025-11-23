# Generated from grammar/matlab.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .matlabParser import matlabParser
else:
    from matlabParser import matlabParser

# This class defines a complete listener for a parse tree produced by matlabParser.
class matlabListener(ParseTreeListener):

    # Enter a parse tree produced by matlabParser#programa.
    def enterPrograma(self, ctx:matlabParser.ProgramaContext):
        pass

    # Exit a parse tree produced by matlabParser#programa.
    def exitPrograma(self, ctx:matlabParser.ProgramaContext):
        pass


    # Enter a parse tree produced by matlabParser#instrucao.
    def enterInstrucao(self, ctx:matlabParser.InstrucaoContext):
        pass

    # Exit a parse tree produced by matlabParser#instrucao.
    def exitInstrucao(self, ctx:matlabParser.InstrucaoContext):
        pass


    # Enter a parse tree produced by matlabParser#instrucaoSimples.
    def enterInstrucaoSimples(self, ctx:matlabParser.InstrucaoSimplesContext):
        pass

    # Exit a parse tree produced by matlabParser#instrucaoSimples.
    def exitInstrucaoSimples(self, ctx:matlabParser.InstrucaoSimplesContext):
        pass


    # Enter a parse tree produced by matlabParser#blocoDeInstrucoes.
    def enterBlocoDeInstrucoes(self, ctx:matlabParser.BlocoDeInstrucoesContext):
        pass

    # Exit a parse tree produced by matlabParser#blocoDeInstrucoes.
    def exitBlocoDeInstrucoes(self, ctx:matlabParser.BlocoDeInstrucoesContext):
        pass


    # Enter a parse tree produced by matlabParser#instrucaoDeBloco.
    def enterInstrucaoDeBloco(self, ctx:matlabParser.InstrucaoDeBlocoContext):
        pass

    # Exit a parse tree produced by matlabParser#instrucaoDeBloco.
    def exitInstrucaoDeBloco(self, ctx:matlabParser.InstrucaoDeBlocoContext):
        pass


    # Enter a parse tree produced by matlabParser#instrucaoIf.
    def enterInstrucaoIf(self, ctx:matlabParser.InstrucaoIfContext):
        pass

    # Exit a parse tree produced by matlabParser#instrucaoIf.
    def exitInstrucaoIf(self, ctx:matlabParser.InstrucaoIfContext):
        pass


    # Enter a parse tree produced by matlabParser#instrucaoFor.
    def enterInstrucaoFor(self, ctx:matlabParser.InstrucaoForContext):
        pass

    # Exit a parse tree produced by matlabParser#instrucaoFor.
    def exitInstrucaoFor(self, ctx:matlabParser.InstrucaoForContext):
        pass


    # Enter a parse tree produced by matlabParser#instrucaoWhile.
    def enterInstrucaoWhile(self, ctx:matlabParser.InstrucaoWhileContext):
        pass

    # Exit a parse tree produced by matlabParser#instrucaoWhile.
    def exitInstrucaoWhile(self, ctx:matlabParser.InstrucaoWhileContext):
        pass


    # Enter a parse tree produced by matlabParser#ladoEsquerdoAtribuicao.
    def enterLadoEsquerdoAtribuicao(self, ctx:matlabParser.LadoEsquerdoAtribuicaoContext):
        pass

    # Exit a parse tree produced by matlabParser#ladoEsquerdoAtribuicao.
    def exitLadoEsquerdoAtribuicao(self, ctx:matlabParser.LadoEsquerdoAtribuicaoContext):
        pass


    # Enter a parse tree produced by matlabParser#atribuicao.
    def enterAtribuicao(self, ctx:matlabParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by matlabParser#atribuicao.
    def exitAtribuicao(self, ctx:matlabParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by matlabParser#expressao.
    def enterExpressao(self, ctx:matlabParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by matlabParser#expressao.
    def exitExpressao(self, ctx:matlabParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by matlabParser#expressaoOuLogico.
    def enterExpressaoOuLogico(self, ctx:matlabParser.ExpressaoOuLogicoContext):
        pass

    # Exit a parse tree produced by matlabParser#expressaoOuLogico.
    def exitExpressaoOuLogico(self, ctx:matlabParser.ExpressaoOuLogicoContext):
        pass


    # Enter a parse tree produced by matlabParser#expressaoELogico.
    def enterExpressaoELogico(self, ctx:matlabParser.ExpressaoELogicoContext):
        pass

    # Exit a parse tree produced by matlabParser#expressaoELogico.
    def exitExpressaoELogico(self, ctx:matlabParser.ExpressaoELogicoContext):
        pass


    # Enter a parse tree produced by matlabParser#expressaoComparacao.
    def enterExpressaoComparacao(self, ctx:matlabParser.ExpressaoComparacaoContext):
        pass

    # Exit a parse tree produced by matlabParser#expressaoComparacao.
    def exitExpressaoComparacao(self, ctx:matlabParser.ExpressaoComparacaoContext):
        pass


    # Enter a parse tree produced by matlabParser#expressaoIntervalo.
    def enterExpressaoIntervalo(self, ctx:matlabParser.ExpressaoIntervaloContext):
        pass

    # Exit a parse tree produced by matlabParser#expressaoIntervalo.
    def exitExpressaoIntervalo(self, ctx:matlabParser.ExpressaoIntervaloContext):
        pass


    # Enter a parse tree produced by matlabParser#expressaoAditiva.
    def enterExpressaoAditiva(self, ctx:matlabParser.ExpressaoAditivaContext):
        pass

    # Exit a parse tree produced by matlabParser#expressaoAditiva.
    def exitExpressaoAditiva(self, ctx:matlabParser.ExpressaoAditivaContext):
        pass


    # Enter a parse tree produced by matlabParser#expressaoMultiplicativa.
    def enterExpressaoMultiplicativa(self, ctx:matlabParser.ExpressaoMultiplicativaContext):
        pass

    # Exit a parse tree produced by matlabParser#expressaoMultiplicativa.
    def exitExpressaoMultiplicativa(self, ctx:matlabParser.ExpressaoMultiplicativaContext):
        pass


    # Enter a parse tree produced by matlabParser#expressaoPotencia.
    def enterExpressaoPotencia(self, ctx:matlabParser.ExpressaoPotenciaContext):
        pass

    # Exit a parse tree produced by matlabParser#expressaoPotencia.
    def exitExpressaoPotencia(self, ctx:matlabParser.ExpressaoPotenciaContext):
        pass


    # Enter a parse tree produced by matlabParser#expressaoUnaria.
    def enterExpressaoUnaria(self, ctx:matlabParser.ExpressaoUnariaContext):
        pass

    # Exit a parse tree produced by matlabParser#expressaoUnaria.
    def exitExpressaoUnaria(self, ctx:matlabParser.ExpressaoUnariaContext):
        pass


    # Enter a parse tree produced by matlabParser#atomo.
    def enterAtomo(self, ctx:matlabParser.AtomoContext):
        pass

    # Exit a parse tree produced by matlabParser#atomo.
    def exitAtomo(self, ctx:matlabParser.AtomoContext):
        pass


    # Enter a parse tree produced by matlabParser#listaArgumentos.
    def enterListaArgumentos(self, ctx:matlabParser.ListaArgumentosContext):
        pass

    # Exit a parse tree produced by matlabParser#listaArgumentos.
    def exitListaArgumentos(self, ctx:matlabParser.ListaArgumentosContext):
        pass


    # Enter a parse tree produced by matlabParser#matriz.
    def enterMatriz(self, ctx:matlabParser.MatrizContext):
        pass

    # Exit a parse tree produced by matlabParser#matriz.
    def exitMatriz(self, ctx:matlabParser.MatrizContext):
        pass


    # Enter a parse tree produced by matlabParser#linhasMatriz.
    def enterLinhasMatriz(self, ctx:matlabParser.LinhasMatrizContext):
        pass

    # Exit a parse tree produced by matlabParser#linhasMatriz.
    def exitLinhasMatriz(self, ctx:matlabParser.LinhasMatrizContext):
        pass


    # Enter a parse tree produced by matlabParser#linha.
    def enterLinha(self, ctx:matlabParser.LinhaContext):
        pass

    # Exit a parse tree produced by matlabParser#linha.
    def exitLinha(self, ctx:matlabParser.LinhaContext):
        pass



del matlabParser