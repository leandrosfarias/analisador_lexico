palavras_reservadas = ['PROGRAM', 'INTEGER', 'BOOLEAN', 'BEGIN', 'END', 'WHILE',
                       'DO', 'READ', 'VAR', 'FALSE', 'TRUE', 'WRITE']
#
operadores_aritmeticos = ['+', '-', '*', '/']
operadores_logicos = ['OR', 'AND']
operador_negacao = '~'
operadores_relacionais = ['<', '>', '<=', '>=', '==', '<>']
simbolos = [';', '.', ':', ',', '(', ')', ':=']


def check_palavra_reservada(txt: str) -> bool:
    return txt.upper() in palavras_reservadas


def is_space(char: str) -> bool:
    return char == ' '


def is_operator(char: str) -> bool:
    # operadores_aritmeticos = ['+', '-', '*', '/']
    # operadores_relacionais = ['<', '>', '<=', '>=', '==', '<>']
    operadores = [
        '+', '-', '*', '/',
        '<', '>', '<=', '>=', '==', '<>',
        ';', '.', ':', ',', '(', ')', ':=',
    ]
    return char in operadores
