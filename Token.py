from TokenType import TokenType


class Token:
    def __init__(self, tipo, atributo: str = ''):
        self.tipo = tipo
        self.atributo = atributo
