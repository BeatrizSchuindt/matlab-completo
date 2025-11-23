class SemanticError:
    def __init__(self, line, column, message):
        self.line = line
        self.column = column
        self.message = message

    def __str__(self):
        return f"Linha {self.line}, coluna {self.column}: {self.message}"
