class Scope:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.symbols = {}

    def define(self, name, type_=None):
        """Define/atribui um símbolo neste escopo."""
        self.symbols[name] = type_

    def resolve_local(self, name):
        """Procura só neste escopo."""
        return self.symbols.get(name)

    def resolve(self, name):
        """Procura neste escopo e nos pais."""
        value = self.symbols.get(name)
        if value is not None:
            return value
        if self.parent is not None:
            return self.parent.resolve(name)
        return None

    def __repr__(self):
        return f"<Scope {self.name}, symbols={list(self.symbols.keys())}>"
