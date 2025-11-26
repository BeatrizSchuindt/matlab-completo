import sys
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

from src.gen.grammar.matlabLexer import matlabLexer
from src.gen.grammar.matlabParser import matlabParser
from src.semantic.matlab_semantico_listener import MatlabSemanticListener
from src.codegen.matlab_codegen_visitor import MatlabCodeGenVisitor
from src.error import RaisingErrorListener, LexicalError, SyntacticError


def compilar_arquivo(input_path: str, output_path: str = "output.py") -> None:
    input_stream = FileStream(input_path, encoding="utf-8")

    # Léxico
    lexer = matlabLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(RaisingErrorListener())

    # Parse
    token_stream = CommonTokenStream(lexer)
    parser = matlabParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(RaisingErrorListener())
    try:
        tree = parser.programa()
    except (LexicalError, SyntacticError) as e:
        print(e)
        sys.exit(1)

    # Semântica
    listener = MatlabSemanticListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    if listener.errors:
        print("Erros semânticos encontrados:")
        for err in listener.errors:
            print(err)
        sys.exit(1)

    # Geração de código Python
    codegen = MatlabCodeGenVisitor(output_file=output_path)
    codegen.visit(tree)
    codegen.save()
    print(f"Código Python gerado em: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python -m src.main_codegen <arquivo.m> [arquivo_saida.py]")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) >= 3 else "output.py"

    compilar_arquivo(input_path, output_path)
