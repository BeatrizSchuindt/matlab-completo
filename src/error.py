"""
Módulo: error.py
Define classes de exceções e listener personalizado para capturar erros
durante as análises léxica e sintática.

Este módulo substitui os listeners padrão do ANTLR4 por um que lança
exceções customizadas, permitindo tratar e exibir erros de forma mais amigável.
"""

from antlr4.error.ErrorListener import ErrorListener


# Exceção para erros durante a análise léxica (scanner)
class LexicalError(Exception):
    """Erro léxico: caractere ou símbolo inválido encontrado."""
    pass


# Exceção para erros durante a análise sintática (parser)
class SyntacticError(Exception):
    """Erro sintático: estrutura incorreta conforme a gramática."""
    pass


class RaisingErrorListener(ErrorListener):
    """
    Listener que intercepta erros do ANTLR e lança exceções personalizadas.

    É adicionado ao lexer e parser no lugar do listener padrão.
    """

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Sobrescreve o método padrão de tratamento de erro.
        Detecta se o erro veio do lexer ou parser e lança a exceção correspondente.
        """
        name = recognizer.__class__.__name__

        if name.endswith("Lexer"):
            # Erro léxico — símbolo não reconhecido
            raise LexicalError(f"ERRO LÉXICO [linha {line}, col {column}]: {msg}")
        else:
            # Erro sintático — estrutura inesperada
            tok = offendingSymbol.text if offendingSymbol else "?"
            raise SyntacticError(
                f"ERRO SINTÁTICO [linha {line}, col {column}] token='{tok}': {msg}"
            )
