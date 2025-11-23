import sys
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

from src.gen.grammar.matlabLexer import matlabLexer
from src.gen.grammar.matlabParser import matlabParser
from src.semantic.matlab_semantic_listener import MatlabSemanticListener
from src.codegen.matlab_codegen_visitor import MatlabCodeGenVisitor


def compilar_arquivo(input_path: str, output_path: str = "output.py") -> None:
    # 1) Lê o arquivo .m
    input_stream = FileStream(input_path, encoding="utf-8")

    # 2) Léxico + parser
    lexer = matlabLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = matlabParser(token_stream)
    tree = parser.programa()

    # 3) Análise semântica
    listener = MatlabSemanticListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    if listener.errors:
        print("Erros semânticos encontrados:")
        for err in listener.errors:
            print(err)
        sys.exit(1)

    # 4) Geração de código Python
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
