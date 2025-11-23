# src/main_semantic.py

import sys
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

from src.gen.grammar.matlabLexer import matlabLexer
from src.gen.grammar.matlabParser import matlabParser
from src.semantic.matlab_semantic_listener import MatlabSemanticListener


def main(argv):
    if len(argv) < 2:
        print("Uso: python -m src.main_semantic <arquivo.m>")
        sys.exit(1)

    input_file = argv[1]

    # 1) Léxico
    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = matlabLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # 2) Sintático
    parser = matlabParser(token_stream)
    tree = parser.programa()

    # 3) Semântico
    listener = MatlabSemanticListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    # 4) Resultado
    if listener.errors:
        print("Foram encontrados erros semânticos:\n")
        for error in listener.errors:
            print(f"- {error}")
        sys.exit(1)
    else:
        print("Análise semântica concluída sem erros.")


if __name__ == "__main__":
    main(sys.argv)
