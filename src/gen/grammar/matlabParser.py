# Generated from grammar/matlab.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,38,247,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,5,0,50,8,0,10,0,12,0,53,9,
        0,1,0,1,0,1,1,1,1,1,1,4,1,60,8,1,11,1,12,1,61,3,1,64,8,1,1,1,1,1,
        4,1,68,8,1,11,1,12,1,69,3,1,72,8,1,1,2,1,2,3,2,76,8,2,1,2,1,2,4,
        2,80,8,2,11,2,12,2,81,3,2,84,8,2,1,3,5,3,87,8,3,10,3,12,3,90,9,3,
        1,4,1,4,1,4,3,4,95,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,104,8,5,10,
        5,12,5,107,9,5,1,5,1,5,3,5,111,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,3,8,131,8,8,1,8,3,8,134,
        8,8,1,9,1,9,1,9,1,9,1,10,1,10,1,11,1,11,1,11,5,11,145,8,11,10,11,
        12,11,148,9,11,1,12,1,12,1,12,5,12,153,8,12,10,12,12,12,156,9,12,
        1,13,1,13,1,13,5,13,161,8,13,10,13,12,13,164,9,13,1,14,1,14,1,14,
        1,14,1,14,3,14,171,8,14,3,14,173,8,14,1,15,1,15,1,15,5,15,178,8,
        15,10,15,12,15,181,9,15,1,16,1,16,1,16,5,16,186,8,16,10,16,12,16,
        189,9,16,1,17,1,17,1,17,3,17,194,8,17,1,18,1,18,1,18,3,18,199,8,
        18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,209,8,19,1,19,1,
        19,1,19,1,19,3,19,215,8,19,1,20,1,20,1,20,5,20,220,8,20,10,20,12,
        20,223,9,20,1,21,1,21,3,21,227,8,21,1,21,1,21,1,22,1,22,1,22,5,22,
        234,8,22,10,22,12,22,237,9,22,1,23,1,23,1,23,5,23,242,8,23,10,23,
        12,23,245,9,23,1,23,0,0,24,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,0,6,1,0,25,26,1,0,23,24,1,0,17,22,
        1,0,8,9,2,0,10,11,13,14,2,0,12,12,15,15,258,0,51,1,0,0,0,2,71,1,
        0,0,0,4,75,1,0,0,0,6,88,1,0,0,0,8,94,1,0,0,0,10,96,1,0,0,0,12,114,
        1,0,0,0,14,121,1,0,0,0,16,133,1,0,0,0,18,135,1,0,0,0,20,139,1,0,
        0,0,22,141,1,0,0,0,24,149,1,0,0,0,26,157,1,0,0,0,28,165,1,0,0,0,
        30,174,1,0,0,0,32,182,1,0,0,0,34,190,1,0,0,0,36,198,1,0,0,0,38,214,
        1,0,0,0,40,216,1,0,0,0,42,224,1,0,0,0,44,230,1,0,0,0,46,238,1,0,
        0,0,48,50,3,2,1,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,
        1,0,0,0,52,54,1,0,0,0,53,51,1,0,0,0,54,55,5,0,0,1,55,1,1,0,0,0,56,
        63,3,8,4,0,57,64,5,31,0,0,58,60,5,37,0,0,59,58,1,0,0,0,60,61,1,0,
        0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,57,1,0,0,0,63,59,
        1,0,0,0,63,64,1,0,0,0,64,72,1,0,0,0,65,72,3,4,2,0,66,68,5,37,0,0,
        67,66,1,0,0,0,68,69,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,72,1,
        0,0,0,71,56,1,0,0,0,71,65,1,0,0,0,71,67,1,0,0,0,72,3,1,0,0,0,73,
        76,3,18,9,0,74,76,3,20,10,0,75,73,1,0,0,0,75,74,1,0,0,0,76,83,1,
        0,0,0,77,84,5,31,0,0,78,80,5,37,0,0,79,78,1,0,0,0,80,81,1,0,0,0,
        81,79,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,77,1,0,0,0,83,79,1,
        0,0,0,84,5,1,0,0,0,85,87,3,2,1,0,86,85,1,0,0,0,87,90,1,0,0,0,88,
        86,1,0,0,0,88,89,1,0,0,0,89,7,1,0,0,0,90,88,1,0,0,0,91,95,3,10,5,
        0,92,95,3,12,6,0,93,95,3,14,7,0,94,91,1,0,0,0,94,92,1,0,0,0,94,93,
        1,0,0,0,95,9,1,0,0,0,96,97,5,1,0,0,97,98,3,20,10,0,98,105,3,6,3,
        0,99,100,5,2,0,0,100,101,3,20,10,0,101,102,3,6,3,0,102,104,1,0,0,
        0,103,99,1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,
        106,110,1,0,0,0,107,105,1,0,0,0,108,109,5,3,0,0,109,111,3,6,3,0,
        110,108,1,0,0,0,110,111,1,0,0,0,111,112,1,0,0,0,112,113,5,6,0,0,
        113,11,1,0,0,0,114,115,5,4,0,0,115,116,5,34,0,0,116,117,5,7,0,0,
        117,118,3,20,10,0,118,119,3,6,3,0,119,120,5,6,0,0,120,13,1,0,0,0,
        121,122,5,5,0,0,122,123,3,20,10,0,123,124,3,6,3,0,124,125,5,6,0,
        0,125,15,1,0,0,0,126,134,5,34,0,0,127,128,5,34,0,0,128,130,5,27,
        0,0,129,131,3,40,20,0,130,129,1,0,0,0,130,131,1,0,0,0,131,132,1,
        0,0,0,132,134,5,28,0,0,133,126,1,0,0,0,133,127,1,0,0,0,134,17,1,
        0,0,0,135,136,3,16,8,0,136,137,5,7,0,0,137,138,3,20,10,0,138,19,
        1,0,0,0,139,140,3,22,11,0,140,21,1,0,0,0,141,146,3,24,12,0,142,143,
        7,0,0,0,143,145,3,24,12,0,144,142,1,0,0,0,145,148,1,0,0,0,146,144,
        1,0,0,0,146,147,1,0,0,0,147,23,1,0,0,0,148,146,1,0,0,0,149,154,3,
        26,13,0,150,151,7,1,0,0,151,153,3,26,13,0,152,150,1,0,0,0,153,156,
        1,0,0,0,154,152,1,0,0,0,154,155,1,0,0,0,155,25,1,0,0,0,156,154,1,
        0,0,0,157,162,3,28,14,0,158,159,7,2,0,0,159,161,3,28,14,0,160,158,
        1,0,0,0,161,164,1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,27,1,
        0,0,0,164,162,1,0,0,0,165,172,3,30,15,0,166,167,5,16,0,0,167,170,
        3,30,15,0,168,169,5,16,0,0,169,171,3,30,15,0,170,168,1,0,0,0,170,
        171,1,0,0,0,171,173,1,0,0,0,172,166,1,0,0,0,172,173,1,0,0,0,173,
        29,1,0,0,0,174,179,3,32,16,0,175,176,7,3,0,0,176,178,3,32,16,0,177,
        175,1,0,0,0,178,181,1,0,0,0,179,177,1,0,0,0,179,180,1,0,0,0,180,
        31,1,0,0,0,181,179,1,0,0,0,182,187,3,34,17,0,183,184,7,4,0,0,184,
        186,3,34,17,0,185,183,1,0,0,0,186,189,1,0,0,0,187,185,1,0,0,0,187,
        188,1,0,0,0,188,33,1,0,0,0,189,187,1,0,0,0,190,193,3,36,18,0,191,
        192,7,5,0,0,192,194,3,36,18,0,193,191,1,0,0,0,193,194,1,0,0,0,194,
        35,1,0,0,0,195,196,7,3,0,0,196,199,3,36,18,0,197,199,3,38,19,0,198,
        195,1,0,0,0,198,197,1,0,0,0,199,37,1,0,0,0,200,201,5,27,0,0,201,
        202,3,20,10,0,202,203,5,28,0,0,203,215,1,0,0,0,204,215,3,42,21,0,
        205,206,5,34,0,0,206,208,5,27,0,0,207,209,3,40,20,0,208,207,1,0,
        0,0,208,209,1,0,0,0,209,210,1,0,0,0,210,215,5,28,0,0,211,215,5,34,
        0,0,212,215,5,35,0,0,213,215,5,33,0,0,214,200,1,0,0,0,214,204,1,
        0,0,0,214,205,1,0,0,0,214,211,1,0,0,0,214,212,1,0,0,0,214,213,1,
        0,0,0,215,39,1,0,0,0,216,221,3,20,10,0,217,218,5,32,0,0,218,220,
        3,20,10,0,219,217,1,0,0,0,220,223,1,0,0,0,221,219,1,0,0,0,221,222,
        1,0,0,0,222,41,1,0,0,0,223,221,1,0,0,0,224,226,5,29,0,0,225,227,
        3,44,22,0,226,225,1,0,0,0,226,227,1,0,0,0,227,228,1,0,0,0,228,229,
        5,30,0,0,229,43,1,0,0,0,230,235,3,46,23,0,231,232,5,31,0,0,232,234,
        3,46,23,0,233,231,1,0,0,0,234,237,1,0,0,0,235,233,1,0,0,0,235,236,
        1,0,0,0,236,45,1,0,0,0,237,235,1,0,0,0,238,243,3,20,10,0,239,240,
        5,32,0,0,240,242,3,20,10,0,241,239,1,0,0,0,242,245,1,0,0,0,243,241,
        1,0,0,0,243,244,1,0,0,0,244,47,1,0,0,0,245,243,1,0,0,0,29,51,61,
        63,69,71,75,81,83,88,94,105,110,130,133,146,154,162,170,172,179,
        187,193,198,208,214,221,226,235,243
    ]

class matlabParser ( Parser ):

    grammarFileName = "matlab.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'elseif'", "'else'", "'for'", 
                     "'while'", "'end'", "'='", "'+'", "'-'", "'*'", "'/'", 
                     "'^'", "'.*'", "'./'", "'.^'", "':'", "'=='", "'~='", 
                     "'<'", "'>'", "'<='", "'>='", "'&'", "'&&'", "'|'", 
                     "'||'", "'('", "')'", "'['", "']'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "KW_IF", "KW_ELSEIF", "KW_ELSE", "KW_FOR", 
                      "KW_WHILE", "KW_END", "ASSIGN", "PLUS", "MINUS", "STAR", 
                      "SLASH", "POW", "DOT_STAR", "DOT_SLASH", "DOT_POW", 
                      "COLON", "EQ", "NEQ", "LT", "GT", "LTE", "GTE", "AND", 
                      "DBL_AND", "OR", "DBL_OR", "LPAREN", "RPAREN", "LBRACK", 
                      "RBRACK", "SEMI", "COMMA", "STRING", "ID", "NUMBER", 
                      "COMMENT", "NEWLINE", "WS" ]

    RULE_programa = 0
    RULE_instrucao = 1
    RULE_instrucaoSimples = 2
    RULE_blocoDeInstrucoes = 3
    RULE_instrucaoDeBloco = 4
    RULE_instrucaoIf = 5
    RULE_instrucaoFor = 6
    RULE_instrucaoWhile = 7
    RULE_ladoEsquerdoAtribuicao = 8
    RULE_atribuicao = 9
    RULE_expressao = 10
    RULE_expressaoOuLogico = 11
    RULE_expressaoELogico = 12
    RULE_expressaoComparacao = 13
    RULE_expressaoIntervalo = 14
    RULE_expressaoAditiva = 15
    RULE_expressaoMultiplicativa = 16
    RULE_expressaoPotencia = 17
    RULE_expressaoUnaria = 18
    RULE_atomo = 19
    RULE_listaArgumentos = 20
    RULE_matriz = 21
    RULE_linhasMatriz = 22
    RULE_linha = 23

    ruleNames =  [ "programa", "instrucao", "instrucaoSimples", "blocoDeInstrucoes", 
                   "instrucaoDeBloco", "instrucaoIf", "instrucaoFor", "instrucaoWhile", 
                   "ladoEsquerdoAtribuicao", "atribuicao", "expressao", 
                   "expressaoOuLogico", "expressaoELogico", "expressaoComparacao", 
                   "expressaoIntervalo", "expressaoAditiva", "expressaoMultiplicativa", 
                   "expressaoPotencia", "expressaoUnaria", "atomo", "listaArgumentos", 
                   "matriz", "linhasMatriz", "linha" ]

    EOF = Token.EOF
    KW_IF=1
    KW_ELSEIF=2
    KW_ELSE=3
    KW_FOR=4
    KW_WHILE=5
    KW_END=6
    ASSIGN=7
    PLUS=8
    MINUS=9
    STAR=10
    SLASH=11
    POW=12
    DOT_STAR=13
    DOT_SLASH=14
    DOT_POW=15
    COLON=16
    EQ=17
    NEQ=18
    LT=19
    GT=20
    LTE=21
    GTE=22
    AND=23
    DBL_AND=24
    OR=25
    DBL_OR=26
    LPAREN=27
    RPAREN=28
    LBRACK=29
    RBRACK=30
    SEMI=31
    COMMA=32
    STRING=33
    ID=34
    NUMBER=35
    COMMENT=36
    NEWLINE=37
    WS=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(matlabParser.EOF, 0)

        def instrucao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matlabParser.InstrucaoContext)
            else:
                return self.getTypedRuleContext(matlabParser.InstrucaoContext,i)


        def getRuleIndex(self):
            return matlabParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = matlabParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 198239585074) != 0):
                self.state = 48
                self.instrucao()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.match(matlabParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrucaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instrucaoDeBloco(self):
            return self.getTypedRuleContext(matlabParser.InstrucaoDeBlocoContext,0)


        def SEMI(self):
            return self.getToken(matlabParser.SEMI, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(matlabParser.NEWLINE)
            else:
                return self.getToken(matlabParser.NEWLINE, i)

        def instrucaoSimples(self):
            return self.getTypedRuleContext(matlabParser.InstrucaoSimplesContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_instrucao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucao" ):
                listener.enterInstrucao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucao" ):
                listener.exitInstrucao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrucao" ):
                return visitor.visitInstrucao(self)
            else:
                return visitor.visitChildren(self)




    def instrucao(self):

        localctx = matlabParser.InstrucaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instrucao)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.instrucaoDeBloco()
                self.state = 63
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 57
                    self.match(matlabParser.SEMI)

                elif la_ == 2:
                    self.state = 59 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 58
                            self.match(matlabParser.NEWLINE)

                        else:
                            raise NoViableAltException(self)
                        self.state = 61 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,1,self._ctx)



                pass
            elif token in [8, 9, 27, 29, 33, 34, 35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.instrucaoSimples()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 3)
                self.state = 67 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 66
                        self.match(matlabParser.NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 69 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrucaoSimplesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atribuicao(self):
            return self.getTypedRuleContext(matlabParser.AtribuicaoContext,0)


        def expressao(self):
            return self.getTypedRuleContext(matlabParser.ExpressaoContext,0)


        def SEMI(self):
            return self.getToken(matlabParser.SEMI, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(matlabParser.NEWLINE)
            else:
                return self.getToken(matlabParser.NEWLINE, i)

        def getRuleIndex(self):
            return matlabParser.RULE_instrucaoSimples

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucaoSimples" ):
                listener.enterInstrucaoSimples(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucaoSimples" ):
                listener.exitInstrucaoSimples(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrucaoSimples" ):
                return visitor.visitInstrucaoSimples(self)
            else:
                return visitor.visitChildren(self)




    def instrucaoSimples(self):

        localctx = matlabParser.InstrucaoSimplesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instrucaoSimples)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 73
                self.atribuicao()
                pass

            elif la_ == 2:
                self.state = 74
                self.expressao()
                pass


            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.state = 77
                self.match(matlabParser.SEMI)
                pass
            elif token in [37]:
                self.state = 79 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 78
                        self.match(matlabParser.NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 81 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlocoDeInstrucoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instrucao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matlabParser.InstrucaoContext)
            else:
                return self.getTypedRuleContext(matlabParser.InstrucaoContext,i)


        def getRuleIndex(self):
            return matlabParser.RULE_blocoDeInstrucoes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlocoDeInstrucoes" ):
                listener.enterBlocoDeInstrucoes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlocoDeInstrucoes" ):
                listener.exitBlocoDeInstrucoes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlocoDeInstrucoes" ):
                return visitor.visitBlocoDeInstrucoes(self)
            else:
                return visitor.visitChildren(self)




    def blocoDeInstrucoes(self):

        localctx = matlabParser.BlocoDeInstrucoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_blocoDeInstrucoes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 198239585074) != 0):
                self.state = 85
                self.instrucao()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrucaoDeBlocoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instrucaoIf(self):
            return self.getTypedRuleContext(matlabParser.InstrucaoIfContext,0)


        def instrucaoFor(self):
            return self.getTypedRuleContext(matlabParser.InstrucaoForContext,0)


        def instrucaoWhile(self):
            return self.getTypedRuleContext(matlabParser.InstrucaoWhileContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_instrucaoDeBloco

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucaoDeBloco" ):
                listener.enterInstrucaoDeBloco(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucaoDeBloco" ):
                listener.exitInstrucaoDeBloco(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrucaoDeBloco" ):
                return visitor.visitInstrucaoDeBloco(self)
            else:
                return visitor.visitChildren(self)




    def instrucaoDeBloco(self):

        localctx = matlabParser.InstrucaoDeBlocoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_instrucaoDeBloco)
        try:
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.instrucaoIf()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.instrucaoFor()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 93
                self.instrucaoWhile()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrucaoIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_IF(self):
            return self.getToken(matlabParser.KW_IF, 0)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matlabParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(matlabParser.ExpressaoContext,i)


        def blocoDeInstrucoes(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matlabParser.BlocoDeInstrucoesContext)
            else:
                return self.getTypedRuleContext(matlabParser.BlocoDeInstrucoesContext,i)


        def KW_END(self):
            return self.getToken(matlabParser.KW_END, 0)

        def KW_ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(matlabParser.KW_ELSEIF)
            else:
                return self.getToken(matlabParser.KW_ELSEIF, i)

        def KW_ELSE(self):
            return self.getToken(matlabParser.KW_ELSE, 0)

        def getRuleIndex(self):
            return matlabParser.RULE_instrucaoIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucaoIf" ):
                listener.enterInstrucaoIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucaoIf" ):
                listener.exitInstrucaoIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrucaoIf" ):
                return visitor.visitInstrucaoIf(self)
            else:
                return visitor.visitChildren(self)




    def instrucaoIf(self):

        localctx = matlabParser.InstrucaoIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_instrucaoIf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(matlabParser.KW_IF)
            self.state = 97
            self.expressao()
            self.state = 98
            self.blocoDeInstrucoes()
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 99
                self.match(matlabParser.KW_ELSEIF)
                self.state = 100
                self.expressao()
                self.state = 101
                self.blocoDeInstrucoes()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 108
                self.match(matlabParser.KW_ELSE)
                self.state = 109
                self.blocoDeInstrucoes()


            self.state = 112
            self.match(matlabParser.KW_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrucaoForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FOR(self):
            return self.getToken(matlabParser.KW_FOR, 0)

        def ID(self):
            return self.getToken(matlabParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(matlabParser.ASSIGN, 0)

        def expressao(self):
            return self.getTypedRuleContext(matlabParser.ExpressaoContext,0)


        def blocoDeInstrucoes(self):
            return self.getTypedRuleContext(matlabParser.BlocoDeInstrucoesContext,0)


        def KW_END(self):
            return self.getToken(matlabParser.KW_END, 0)

        def getRuleIndex(self):
            return matlabParser.RULE_instrucaoFor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucaoFor" ):
                listener.enterInstrucaoFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucaoFor" ):
                listener.exitInstrucaoFor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrucaoFor" ):
                return visitor.visitInstrucaoFor(self)
            else:
                return visitor.visitChildren(self)




    def instrucaoFor(self):

        localctx = matlabParser.InstrucaoForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_instrucaoFor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(matlabParser.KW_FOR)
            self.state = 115
            self.match(matlabParser.ID)
            self.state = 116
            self.match(matlabParser.ASSIGN)
            self.state = 117
            self.expressao()
            self.state = 118
            self.blocoDeInstrucoes()
            self.state = 119
            self.match(matlabParser.KW_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrucaoWhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_WHILE(self):
            return self.getToken(matlabParser.KW_WHILE, 0)

        def expressao(self):
            return self.getTypedRuleContext(matlabParser.ExpressaoContext,0)


        def blocoDeInstrucoes(self):
            return self.getTypedRuleContext(matlabParser.BlocoDeInstrucoesContext,0)


        def KW_END(self):
            return self.getToken(matlabParser.KW_END, 0)

        def getRuleIndex(self):
            return matlabParser.RULE_instrucaoWhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucaoWhile" ):
                listener.enterInstrucaoWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucaoWhile" ):
                listener.exitInstrucaoWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrucaoWhile" ):
                return visitor.visitInstrucaoWhile(self)
            else:
                return visitor.visitChildren(self)




    def instrucaoWhile(self):

        localctx = matlabParser.InstrucaoWhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_instrucaoWhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(matlabParser.KW_WHILE)
            self.state = 122
            self.expressao()
            self.state = 123
            self.blocoDeInstrucoes()
            self.state = 124
            self.match(matlabParser.KW_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LadoEsquerdoAtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(matlabParser.ID, 0)

        def LPAREN(self):
            return self.getToken(matlabParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(matlabParser.RPAREN, 0)

        def listaArgumentos(self):
            return self.getTypedRuleContext(matlabParser.ListaArgumentosContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_ladoEsquerdoAtribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLadoEsquerdoAtribuicao" ):
                listener.enterLadoEsquerdoAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLadoEsquerdoAtribuicao" ):
                listener.exitLadoEsquerdoAtribuicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLadoEsquerdoAtribuicao" ):
                return visitor.visitLadoEsquerdoAtribuicao(self)
            else:
                return visitor.visitChildren(self)




    def ladoEsquerdoAtribuicao(self):

        localctx = matlabParser.LadoEsquerdoAtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ladoEsquerdoAtribuicao)
        self._la = 0 # Token type
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.match(matlabParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.match(matlabParser.ID)
                self.state = 128
                self.match(matlabParser.LPAREN)
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 60800631552) != 0):
                    self.state = 129
                    self.listaArgumentos()


                self.state = 132
                self.match(matlabParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ladoEsquerdoAtribuicao(self):
            return self.getTypedRuleContext(matlabParser.LadoEsquerdoAtribuicaoContext,0)


        def ASSIGN(self):
            return self.getToken(matlabParser.ASSIGN, 0)

        def expressao(self):
            return self.getTypedRuleContext(matlabParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtribuicao" ):
                return visitor.visitAtribuicao(self)
            else:
                return visitor.visitChildren(self)




    def atribuicao(self):

        localctx = matlabParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.ladoEsquerdoAtribuicao()
            self.state = 136
            self.match(matlabParser.ASSIGN)
            self.state = 137
            self.expressao()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressaoOuLogico(self):
            return self.getTypedRuleContext(matlabParser.ExpressaoOuLogicoContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao" ):
                listener.enterExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao" ):
                listener.exitExpressao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressao" ):
                return visitor.visitExpressao(self)
            else:
                return visitor.visitChildren(self)




    def expressao(self):

        localctx = matlabParser.ExpressaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expressao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.expressaoOuLogico()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoOuLogicoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressaoELogico(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matlabParser.ExpressaoELogicoContext)
            else:
                return self.getTypedRuleContext(matlabParser.ExpressaoELogicoContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(matlabParser.OR)
            else:
                return self.getToken(matlabParser.OR, i)

        def DBL_OR(self, i:int=None):
            if i is None:
                return self.getTokens(matlabParser.DBL_OR)
            else:
                return self.getToken(matlabParser.DBL_OR, i)

        def getRuleIndex(self):
            return matlabParser.RULE_expressaoOuLogico

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressaoOuLogico" ):
                listener.enterExpressaoOuLogico(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressaoOuLogico" ):
                listener.exitExpressaoOuLogico(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressaoOuLogico" ):
                return visitor.visitExpressaoOuLogico(self)
            else:
                return visitor.visitChildren(self)




    def expressaoOuLogico(self):

        localctx = matlabParser.ExpressaoOuLogicoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expressaoOuLogico)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.expressaoELogico()
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25 or _la==26:
                self.state = 142
                _la = self._input.LA(1)
                if not(_la==25 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 143
                self.expressaoELogico()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoELogicoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressaoComparacao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matlabParser.ExpressaoComparacaoContext)
            else:
                return self.getTypedRuleContext(matlabParser.ExpressaoComparacaoContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(matlabParser.AND)
            else:
                return self.getToken(matlabParser.AND, i)

        def DBL_AND(self, i:int=None):
            if i is None:
                return self.getTokens(matlabParser.DBL_AND)
            else:
                return self.getToken(matlabParser.DBL_AND, i)

        def getRuleIndex(self):
            return matlabParser.RULE_expressaoELogico

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressaoELogico" ):
                listener.enterExpressaoELogico(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressaoELogico" ):
                listener.exitExpressaoELogico(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressaoELogico" ):
                return visitor.visitExpressaoELogico(self)
            else:
                return visitor.visitChildren(self)




    def expressaoELogico(self):

        localctx = matlabParser.ExpressaoELogicoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expressaoELogico)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.expressaoComparacao()
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23 or _la==24:
                self.state = 150
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 151
                self.expressaoComparacao()
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoComparacaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressaoIntervalo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matlabParser.ExpressaoIntervaloContext)
            else:
                return self.getTypedRuleContext(matlabParser.ExpressaoIntervaloContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(matlabParser.EQ)
            else:
                return self.getToken(matlabParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(matlabParser.NEQ)
            else:
                return self.getToken(matlabParser.NEQ, i)

        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(matlabParser.LT)
            else:
                return self.getToken(matlabParser.LT, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(matlabParser.GT)
            else:
                return self.getToken(matlabParser.GT, i)

        def LTE(self, i:int=None):
            if i is None:
                return self.getTokens(matlabParser.LTE)
            else:
                return self.getToken(matlabParser.LTE, i)

        def GTE(self, i:int=None):
            if i is None:
                return self.getTokens(matlabParser.GTE)
            else:
                return self.getToken(matlabParser.GTE, i)

        def getRuleIndex(self):
            return matlabParser.RULE_expressaoComparacao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressaoComparacao" ):
                listener.enterExpressaoComparacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressaoComparacao" ):
                listener.exitExpressaoComparacao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressaoComparacao" ):
                return visitor.visitExpressaoComparacao(self)
            else:
                return visitor.visitChildren(self)




    def expressaoComparacao(self):

        localctx = matlabParser.ExpressaoComparacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expressaoComparacao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.expressaoIntervalo()
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8257536) != 0):
                self.state = 158
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8257536) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 159
                self.expressaoIntervalo()
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoIntervaloContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressaoAditiva(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matlabParser.ExpressaoAditivaContext)
            else:
                return self.getTypedRuleContext(matlabParser.ExpressaoAditivaContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(matlabParser.COLON)
            else:
                return self.getToken(matlabParser.COLON, i)

        def getRuleIndex(self):
            return matlabParser.RULE_expressaoIntervalo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressaoIntervalo" ):
                listener.enterExpressaoIntervalo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressaoIntervalo" ):
                listener.exitExpressaoIntervalo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressaoIntervalo" ):
                return visitor.visitExpressaoIntervalo(self)
            else:
                return visitor.visitChildren(self)




    def expressaoIntervalo(self):

        localctx = matlabParser.ExpressaoIntervaloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expressaoIntervalo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.expressaoAditiva()
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 166
                self.match(matlabParser.COLON)
                self.state = 167
                self.expressaoAditiva()
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 168
                    self.match(matlabParser.COLON)
                    self.state = 169
                    self.expressaoAditiva()




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoAditivaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressaoMultiplicativa(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matlabParser.ExpressaoMultiplicativaContext)
            else:
                return self.getTypedRuleContext(matlabParser.ExpressaoMultiplicativaContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(matlabParser.PLUS)
            else:
                return self.getToken(matlabParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(matlabParser.MINUS)
            else:
                return self.getToken(matlabParser.MINUS, i)

        def getRuleIndex(self):
            return matlabParser.RULE_expressaoAditiva

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressaoAditiva" ):
                listener.enterExpressaoAditiva(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressaoAditiva" ):
                listener.exitExpressaoAditiva(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressaoAditiva" ):
                return visitor.visitExpressaoAditiva(self)
            else:
                return visitor.visitChildren(self)




    def expressaoAditiva(self):

        localctx = matlabParser.ExpressaoAditivaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expressaoAditiva)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.expressaoMultiplicativa()
            self.state = 179
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 175
                    _la = self._input.LA(1)
                    if not(_la==8 or _la==9):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 176
                    self.expressaoMultiplicativa() 
                self.state = 181
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoMultiplicativaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressaoPotencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matlabParser.ExpressaoPotenciaContext)
            else:
                return self.getTypedRuleContext(matlabParser.ExpressaoPotenciaContext,i)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(matlabParser.STAR)
            else:
                return self.getToken(matlabParser.STAR, i)

        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(matlabParser.SLASH)
            else:
                return self.getToken(matlabParser.SLASH, i)

        def DOT_STAR(self, i:int=None):
            if i is None:
                return self.getTokens(matlabParser.DOT_STAR)
            else:
                return self.getToken(matlabParser.DOT_STAR, i)

        def DOT_SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(matlabParser.DOT_SLASH)
            else:
                return self.getToken(matlabParser.DOT_SLASH, i)

        def getRuleIndex(self):
            return matlabParser.RULE_expressaoMultiplicativa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressaoMultiplicativa" ):
                listener.enterExpressaoMultiplicativa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressaoMultiplicativa" ):
                listener.exitExpressaoMultiplicativa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressaoMultiplicativa" ):
                return visitor.visitExpressaoMultiplicativa(self)
            else:
                return visitor.visitChildren(self)




    def expressaoMultiplicativa(self):

        localctx = matlabParser.ExpressaoMultiplicativaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expressaoMultiplicativa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.expressaoPotencia()
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 27648) != 0):
                self.state = 183
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 27648) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 184
                self.expressaoPotencia()
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoPotenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressaoUnaria(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matlabParser.ExpressaoUnariaContext)
            else:
                return self.getTypedRuleContext(matlabParser.ExpressaoUnariaContext,i)


        def POW(self):
            return self.getToken(matlabParser.POW, 0)

        def DOT_POW(self):
            return self.getToken(matlabParser.DOT_POW, 0)

        def getRuleIndex(self):
            return matlabParser.RULE_expressaoPotencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressaoPotencia" ):
                listener.enterExpressaoPotencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressaoPotencia" ):
                listener.exitExpressaoPotencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressaoPotencia" ):
                return visitor.visitExpressaoPotencia(self)
            else:
                return visitor.visitChildren(self)




    def expressaoPotencia(self):

        localctx = matlabParser.ExpressaoPotenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expressaoPotencia)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.expressaoUnaria()
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12 or _la==15:
                self.state = 191
                _la = self._input.LA(1)
                if not(_la==12 or _la==15):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 192
                self.expressaoUnaria()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoUnariaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressaoUnaria(self):
            return self.getTypedRuleContext(matlabParser.ExpressaoUnariaContext,0)


        def PLUS(self):
            return self.getToken(matlabParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(matlabParser.MINUS, 0)

        def atomo(self):
            return self.getTypedRuleContext(matlabParser.AtomoContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_expressaoUnaria

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressaoUnaria" ):
                listener.enterExpressaoUnaria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressaoUnaria" ):
                listener.exitExpressaoUnaria(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressaoUnaria" ):
                return visitor.visitExpressaoUnaria(self)
            else:
                return visitor.visitChildren(self)




    def expressaoUnaria(self):

        localctx = matlabParser.ExpressaoUnariaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expressaoUnaria)
        self._la = 0 # Token type
        try:
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                _la = self._input.LA(1)
                if not(_la==8 or _la==9):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 196
                self.expressaoUnaria()
                pass
            elif token in [27, 29, 33, 34, 35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.atomo()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(matlabParser.LPAREN, 0)

        def expressao(self):
            return self.getTypedRuleContext(matlabParser.ExpressaoContext,0)


        def RPAREN(self):
            return self.getToken(matlabParser.RPAREN, 0)

        def matriz(self):
            return self.getTypedRuleContext(matlabParser.MatrizContext,0)


        def ID(self):
            return self.getToken(matlabParser.ID, 0)

        def listaArgumentos(self):
            return self.getTypedRuleContext(matlabParser.ListaArgumentosContext,0)


        def NUMBER(self):
            return self.getToken(matlabParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(matlabParser.STRING, 0)

        def getRuleIndex(self):
            return matlabParser.RULE_atomo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomo" ):
                listener.enterAtomo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomo" ):
                listener.exitAtomo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomo" ):
                return visitor.visitAtomo(self)
            else:
                return visitor.visitChildren(self)




    def atomo(self):

        localctx = matlabParser.AtomoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_atomo)
        self._la = 0 # Token type
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.match(matlabParser.LPAREN)
                self.state = 201
                self.expressao()
                self.state = 202
                self.match(matlabParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.matriz()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 205
                self.match(matlabParser.ID)
                self.state = 206
                self.match(matlabParser.LPAREN)
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 60800631552) != 0):
                    self.state = 207
                    self.listaArgumentos()


                self.state = 210
                self.match(matlabParser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 211
                self.match(matlabParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 212
                self.match(matlabParser.NUMBER)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 213
                self.match(matlabParser.STRING)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matlabParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(matlabParser.ExpressaoContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(matlabParser.COMMA)
            else:
                return self.getToken(matlabParser.COMMA, i)

        def getRuleIndex(self):
            return matlabParser.RULE_listaArgumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaArgumentos" ):
                listener.enterListaArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaArgumentos" ):
                listener.exitListaArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaArgumentos" ):
                return visitor.visitListaArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def listaArgumentos(self):

        localctx = matlabParser.ListaArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_listaArgumentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.expressao()
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 217
                self.match(matlabParser.COMMA)
                self.state = 218
                self.expressao()
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrizContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(matlabParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(matlabParser.RBRACK, 0)

        def linhasMatriz(self):
            return self.getTypedRuleContext(matlabParser.LinhasMatrizContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_matriz

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatriz" ):
                listener.enterMatriz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatriz" ):
                listener.exitMatriz(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatriz" ):
                return visitor.visitMatriz(self)
            else:
                return visitor.visitChildren(self)




    def matriz(self):

        localctx = matlabParser.MatrizContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_matriz)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(matlabParser.LBRACK)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 60800631552) != 0):
                self.state = 225
                self.linhasMatriz()


            self.state = 228
            self.match(matlabParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinhasMatrizContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def linha(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matlabParser.LinhaContext)
            else:
                return self.getTypedRuleContext(matlabParser.LinhaContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(matlabParser.SEMI)
            else:
                return self.getToken(matlabParser.SEMI, i)

        def getRuleIndex(self):
            return matlabParser.RULE_linhasMatriz

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLinhasMatriz" ):
                listener.enterLinhasMatriz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLinhasMatriz" ):
                listener.exitLinhasMatriz(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLinhasMatriz" ):
                return visitor.visitLinhasMatriz(self)
            else:
                return visitor.visitChildren(self)




    def linhasMatriz(self):

        localctx = matlabParser.LinhasMatrizContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_linhasMatriz)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.linha()
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 231
                self.match(matlabParser.SEMI)
                self.state = 232
                self.linha()
                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinhaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matlabParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(matlabParser.ExpressaoContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(matlabParser.COMMA)
            else:
                return self.getToken(matlabParser.COMMA, i)

        def getRuleIndex(self):
            return matlabParser.RULE_linha

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLinha" ):
                listener.enterLinha(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLinha" ):
                listener.exitLinha(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLinha" ):
                return visitor.visitLinha(self)
            else:
                return visitor.visitChildren(self)




    def linha(self):

        localctx = matlabParser.LinhaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_linha)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.expressao()
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 239
                self.match(matlabParser.COMMA)
                self.state = 240
                self.expressao()
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





