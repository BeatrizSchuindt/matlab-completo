grammar matlab;

programa: instrucao* EOF;

instrucao
    : instrucaoDeBloco (SEMI | NEWLINE+)?
    | instrucaoSimples
    | NEWLINE+
    ;

instrucaoSimples
    : (atribuicao | expressao) (SEMI | NEWLINE+)
    ;

blocoDeInstrucoes
    : instrucao*
    ;

instrucaoDeBloco
    : instrucaoIf
    | instrucaoFor
    | instrucaoWhile
    ;

instrucaoIf
    : KW_IF expressao blocoDeInstrucoes
      (KW_ELSEIF expressao blocoDeInstrucoes)*
      (KW_ELSE blocoDeInstrucoes)?
      KW_END
    ;

instrucaoFor
    : KW_FOR ID ASSIGN expressao blocoDeInstrucoes KW_END
    ;

instrucaoWhile
    : KW_WHILE expressao blocoDeInstrucoes KW_END
    ;

ladoEsquerdoAtribuicao
    : ID
    | ID LPAREN listaArgumentos? RPAREN
    ;

atribuicao
    : ladoEsquerdoAtribuicao ASSIGN expressao
    ;

expressao
    : expressaoOuLogico
    ;

expressaoOuLogico
    : expressaoELogico ( (OR | DBL_OR) expressaoELogico )*
    ;

expressaoELogico
    : expressaoComparacao ( (AND | DBL_AND) expressaoComparacao )*
    ;

expressaoComparacao
    : expressaoIntervalo ( (EQ | NEQ | LT | GT | LTE | GTE) expressaoIntervalo )*
    ;

expressaoIntervalo
    : expressaoAditiva ( COLON expressaoAditiva ( COLON expressaoAditiva )? )?
    ;

expressaoAditiva
    : expressaoMultiplicativa ( (PLUS | MINUS) expressaoMultiplicativa )*
    ;

expressaoMultiplicativa
    : expressaoPotencia ( (STAR | SLASH | DOT_STAR | DOT_SLASH) expressaoPotencia )*
    ;

expressaoPotencia
    : expressaoUnaria ( (POW | DOT_POW) expressaoUnaria )?
    ;

expressaoUnaria
    : (PLUS | MINUS) expressaoUnaria
    | atomo
    ;

atomo
    : LPAREN expressao RPAREN
    | matriz
    | ID LPAREN listaArgumentos? RPAREN
    | ID
    | NUMBER
    | STRING
    ;

listaArgumentos
    : expressao (COMMA expressao)*
    ;

matriz
    : LBRACK linhasMatriz? RBRACK
    ;

linhasMatriz
    : linha (SEMI linha)*
    ;

linha
    : expressao (COMMA expressao)*
    ;

KW_IF:      'if';
KW_ELSEIF:  'elseif';
KW_ELSE:    'else';
KW_FOR:     'for';
KW_WHILE:   'while';
KW_END:     'end';

ASSIGN:     '=';
PLUS:       '+';
MINUS:      '-';
STAR:       '*';
SLASH:      '/';
POW:        '^';
DOT_STAR:   '.*';
DOT_SLASH:  './';
DOT_POW:    '.^';
COLON:      ':';

EQ:         '==';
NEQ:        '~=';
LT:         '<';
GT:         '>';
LTE:        '<=';
GTE:        '>=';

AND:        '&';
DBL_AND:    '&&';
OR:         '|';
DBL_OR:     '||';

LPAREN:     '(';
RPAREN:     ')';
LBRACK:     '[';
RBRACK:     ']';
SEMI:       ';';
COMMA:      ',';

STRING:     '\'' ( ~'\'' | '\'\'' )* '\'' ;

ID:         LETTER (LETTER | DIGIT | '_')* ;

NUMBER:     DIGIT+ ('.' DIGIT+)? ( ('e' | 'E') (PLUS | MINUS)? DIGIT+ )? ;

COMMENT:    '%' ~[\r\n]* -> skip;

NEWLINE:    ('\r'? '\n') | '\r';

WS:         [ \t]+ -> skip;

fragment LETTER: [a-zA-Z];
fragment DIGIT:  [0-9];