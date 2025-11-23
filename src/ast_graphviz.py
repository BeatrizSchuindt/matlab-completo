"""
Módulo: ast_graphviz.py
Responsável por gerar representações gráficas da árvore sintática (parse tree)
em formato PNG e SVG utilizando a biblioteca Graphviz.

Utilizado após o processo de análise sintática (parser) para visualizar
a estrutura hierárquica do código-fonte analisado.
"""

import os, html
from antlr4.tree.Tree import TerminalNode
from graphviz import Digraph


def _node_id(obj) -> str:
    """Gera um identificador único para cada nó com base no id do objeto."""
    return f"n{id(obj)}"


def render_tree_png(tree, parser, out_path_png: str) -> str:
    """
    Gera uma imagem PNG da árvore sintática (parse tree).

    Parâmetros:
        tree : objeto retornado pelo parser (árvore sintática)
        parser : instância do parser ANTLR
        out_path_png : caminho do arquivo de saída .png

    Retorna:
        Caminho final do arquivo PNG gerado.

    Observação:
        É necessário ter o Graphviz instalado e o pacote 'graphviz' no Python.
    """

    # Configuração visual do grafo (nós e arestas)
    dot = Digraph(
        "ParseTree",
        node_attr={
            "shape": "box",
            "fontname": "Consolas",
            "fontsize": "10",
            "style": "rounded,filled",
        },
        edge_attr={"arrowsize": "0.6"},
        graph_attr={
            "ranksep": "0.3",
            "nodesep": "0.25",
            "labelloc": "t",
        },
    )

    def add(node):
        """Adiciona recursivamente cada nó da árvore ao grafo DOT."""
        nid = _node_id(node)

        # Se o nó for terminal (token), usa cor azul claro
        if isinstance(node, TerminalNode):
            text = node.getText()
            label = f"'{html.escape(text)}'"
            dot.node(nid, label, fillcolor="#eaf5ff")  # tokens = azul clarinho
        else:
            # Nó não-terminal (regra da gramática)
            rule = parser.ruleNames[node.getRuleIndex()]
            dot.node(nid, rule, fillcolor="#f6f6f6")    # regras = cinza claro

        # Adiciona as ligações entre os nós (arestas)
        for i in range(node.getChildCount()):
            ch = node.getChild(i)
            dot.edge(nid, _node_id(ch))
            add(ch)

    # Chama a função recursiva
    add(tree)

    # Gera o arquivo PNG final
    base, _ = os.path.splitext(out_path_png)
    dot.format = "png"
    out = dot.render(filename=base, cleanup=True)
    return out


def render_tree_svg(tree, parser, out_path_svg: str) -> str:
    """
    Gera uma imagem SVG da árvore sintática (parse tree).

    É similar ao método anterior, mas gera o resultado em formato vetorial (.svg).
    """
    base, _ = os.path.splitext(out_path_svg)

    dot = Digraph(
        "ParseTree",
        node_attr={
            "shape": "box",
            "fontname": "Consolas",
            "fontsize": "10",
            "style": "rounded,filled",
        },
        edge_attr={"arrowsize": "0.6"},
        graph_attr={"ranksep": "0.3", "nodesep": "0.25", "labelloc": "t"},
    )

    def add(node):
        nid = f"n{id(node)}"
        if isinstance(node, TerminalNode):
            label = f"'{html.escape(node.getText())}'"
            dot.node(nid, label, fillcolor="#eaf5ff")
        else:
            rule = parser.ruleNames[node.getRuleIndex()]
            dot.node(nid, rule, fillcolor="#f6f6f6")

        for i in range(node.getChildCount()):
            ch = node.getChild(i)
            dot.edge(nid, f"n{id(ch)}")
            add(ch)

    add(tree)
    dot.format = "svg"
    out = dot.render(filename=base, cleanup=True)
    return out
