

class Gramatica():

    regras = {
        'palavras_reservadas':    'PROGRAM|INTEGER|BOOLEAN|BEGIN|END|WHILE|DO|READ|VAR|FALSE|TRUE|WRITE',
        'simbolos':               ';|.|:=|,|(|)|:',
        'operadores_aritmeticos': '+|-|*|/',
        'operador_negacao':       '~',
        'numeros':                '[0-9]+',
        'operadores_relacionais': '<|<=|>|>=|==|<>',
        'operadores_logicos':     'OR|AND',
        'indicadores':            '^[a-z|A-Z]+[a-z|A-Z|0-9]*'
    }

    def __init__(self):
        self.gramatica = self.une_regras()

    def une_regras(self):
        regex = ''
        for regra in self.regras.values():
            regex += f'{regra}|'
        regex = regex[:-1]
        return regex
