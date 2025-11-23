"""
Módulo: main.py
Ponto de entrada principal do compilador.

Responsável por:
- Ler o arquivo fonte (.m);
- Realizar a análise léxica e sintática com ANTLR4;
- Gerar a árvore sintática abstrata (AST);
- Renderizar a árvore em PNG e SVG;
- Exibir mensagens de erro e sucesso.

Execução:
    python -m src.main exemplos/triangulos_ok.m
"""

import os, sys
from antlr4 import FileStream, CommonTokenStream

# Importa tratamento de erros customizado
from src.error import RaisingErrorListener, LexicalError, SyntacticError

# Importa as classes geradas automaticamente pelo ANTLR (lexer e parser)
from src.gen.grammar.matlabLexer import matlabLexer
from src.gen.grammar.matlabParser import matlabParser

# Importa funções para renderizar a árvore sintática em imagem
from src.ast_graphviz import render_tree_png, render_tree_svg


def parse_file(path):
    """
    Função auxiliar para ler e processar um arquivo-fonte (.m).

    Retorna:
        (tree, parser) — árvore sintática e instância do parser.
    """
    input_stream = FileStream(path, encoding="utf-8")
    lexer = matlabLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = matlabParser(tokens)

    # Remove listeners padrão e adiciona o personalizado
    lexer.removeErrorListeners()
    parser.removeErrorListeners()
    listener = RaisingErrorListener()
    lexer.addErrorListener(listener)
    parser.addErrorListener(listener)

    # Chama a regra inicial definida na gramática (programa)
    tree = parser.programa()
    return tree, parser


def main():
    """Função principal: executa o compilador via linha de comando."""
    if len(sys.argv) < 2:
        print("Uso:\n  python -m src.main caminho\\arquivo.m")
        sys.exit(64)

    src_path = sys.argv[1]

    try:
        # Executa análise léxica e sintática
        tree, parser = parse_file(src_path)
    except LexicalError as e:
        print(e)
        sys.exit(65)
    except SyntacticError as e:
        print(e)
        sys.exit(66)

    # Caminhos de saída para os gráficos da árvore
    base, _ = os.path.splitext(src_path)
    png_path = base + ".tree.png"
    svg_path = base + ".tree.svg"

    # Gera a visualização da árvore
    png_out = render_tree_png(tree, parser, png_path)
    print(f"✅ Árvore sintática gerada: {png_out}")

    try:
        svg_out = render_tree_svg(tree, parser, svg_path)
        print(f"✅ Versão vetorial: {svg_out}")
    except Exception:
        # Geração SVG é opcional (pode falhar se o Graphviz não suportar SVG)
        pass


# Executa o compilador se o arquivo for chamado diretamente
if __name__ == "__main__":
    main()
