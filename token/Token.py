

class Token():

    tipos = {
        'ID':      ("ID", ""),
        '+':       ("OPAD", "MAIS"),
        '-':       ("OPAD", "MENOS"),
        '*':       ("OPMULT", "VEZES"),
        '/':       ("OPMULT", "DIV"),
        'OR':      ("OPLOG", "OR"),
        'AND':     ("OPLOG", "AND"),
        '~':       ("OPNEG", "NEG"),
        '<':       ("OPREL", "MENOR"),
        '<=':      ("OPREL", "MENIG"),
        '>':       ("OPREL", "MAIOR"),
        '>=':      ("OPREL", "MAIG"),
        '==':      ("OPREL", "IGUAL"),
        '<>':      ("OPREL", "DIFER"),
        ';':       "PVIG",
        '.':       "PONTO",
        ':':       "DPONTOS",
        ',':       "VIG",
        '(':       "ABPAR",
        ')':       "FPAR",
        ':=':      "ATRIB",
        'PROGRAM': "PROGRAM",
        'INTEGER': "INTEGER",
        'BOOLEAN': "BOOLEAN",
        'BEGIN':   "BEGIN",
        'END':     "END",
        'WHILE':   "WHILE",
        'DO':      "DO",
        'READ':    "READ",
        'VAR':     "VAR",
        'FALSE':   "FALSE",
        'TRUE':    "TRUE",
        'WRITE':   "WRITE",
        'STRING':  "CADEIA"
    }


    def __init__(self, caracter):
        self.caracter = caracter
        self.tipo = self.define_tipo()


    def define_tipo(self):
        for simbolo in Token.tipos.keys():
            if self.caracter == simbolo:
                return Token.tipos[simbolo]
            else:
                if self.caracter[0] == '"' and self.caracter[-1] == '"':
                    return Token.tipos['STRING']
                else:
                    tipo_aux = Token.tipos['ID']
                    tipo_aux[1] = self.caracter
                    return tipo_aux


    def imprimir(self):
        if type(self.tipo) == tuple:
            return print(f'<{self.tipo[0]}, {self.tipo[1]}>')
        else:
            return print(f'<{self.tipo}>')
