from Scanner import Scanner
from Token import Token
from TokenType import TokenType
import re
from auxiliares import is_space, is_operator, check_palavra_reservada, \
    operadores_aritmeticos, operadores_logicos, \
    operador_negacao, operadores_relacionais, simbolos

scanner = Scanner('teste.txt')
estado = 0
termo = ''
token = None
tokens = {}

current_char = ''


def criar_token(termo, tipo, atributo: str = ''):
    tokens[f'{termo}'] = (f'{tipo}', f'{atributo}')
    # if tipo == TokenType.ID:
    #     if check_palavra_reservada(termo):
    #         tokens[f'{termo}'] = (f'{termo}', '')
    #     else:
    #         tokens[f'{termo}'] = (f'{TokenType.ID}', f'{termo}')
    # else:
    #     tokens[f'{termo}'] = (f'{tipo}', f'{termo}')


while scanner.has_next():
    current_char = scanner.read_char().upper()
    if re.match(r'[A-Z]', current_char):
        termo += current_char
        estado = 1
        # atualizar o caracter corrente
        # current_char = ''
    elif re.match(r'\d', current_char):
        termo += current_char
        estado = 3
    elif re.match(r'\s', current_char):
        continue
    elif current_char in simbolos:
        termo += current_char
        estado = 5
    else:
        termo += current_char
        estado = 5

    # Estado q1, representa que começou com letra [a...z]
    if estado == 1:
        if re.match(r'[A-Z\d]', current_char):
            # aqui está montando o termo
            termo += current_char
            continue
        else:
            if re.match(r'PROGRAM|INTEGER|BOOLEAN|BEGIN|END|WHILE|DO|READ|VAR|FALSE|TRUE|WRITE', termo):
                # criar_token(termo, termo)
                estado = 2
                continue
            criar_token(termo, TokenType.ID)
            termo = ''
    elif estado == 2:
        criar_token(termo, termo)
    elif estado == 3:
        if re.match(r'\d', current_char):
            termo += current_char
        else:
            estado = 0
            criar_token(termo, TokenType.NUMERO)
            termo = ''
    elif estado == 5:
        if termo.strip() in simbolos:
            tipo = {
                ';': TokenType.PVIG,
                '.': TokenType.PONTO,
                ':': TokenType.DPONTOS,
                ',': TokenType.VIG,
                '(': TokenType.ABPAR,
                ')': TokenType.FPAR,
                ':=': TokenType.ATRIB
            }.get(termo.strip())
            if tipo == ':':
                continue
            criar_token(termo.strip(), tipo)
            termo = ''
            estado = 0
        elif termo.strip() in operadores_aritmeticos:
            tipo = {
                '+': TokenType.OPAD,
                '-': TokenType.OPAD,
                '*': TokenType.OPMULT,
                '/': TokenType.OPMULT
            }.get(termo.strip())
            criar_token(termo.strip(), tipo)
            termo = ''
            estado = 0
        elif termo.strip() in operadores_relacionais:
            tipo = {
                '<': TokenType.OPREL,
                '>': TokenType.OPREL,
                '<=': TokenType.OPREL,
                '>=': TokenType.OPREL,
                '<>': TokenType.OPREL,
                '==': TokenType.OPREL
            }.get(termo.strip())
            criar_token(termo.strip(), tipo)
            termo

for k, v in tokens.items():
    # if v[0] == TokenType.ID:
    #     print(f'<IDENTIFICADOR,{v[1]}> ', end='')
    if v[0] == 'TokenType.ID':
        print(f'<identificador, "{v[1]}"> ', end='')
    elif v[0] == 'TokenType.OPAD' and v[1] == 'MAIS':
        print(f'<ADICAO> ', end='')
    elif v[0] == 'TokenType.OPAD' and v[1] == 'MENOS':
        print(f'<SUBTRACAO> ', end='')
    elif v[0] == 'TokenType.OPMULT' and v[1] == 'VEZES':
        print(f'<MULTIPLICACAO> ', end='')
    elif v[0] == 'TokenType.OPMULT' and v[1] == 'DIV':
        print(f'<DIVISAO> ', end='')
    elif v[0] == 'TokenType.PVIG':
        print(f'<PONTOVIRGULA> ', end='')
    elif v[0] == 'TokenType.ATRIB':
        print(f'<ATRIBUICAO> ', end='')
    elif v[0] == 'TokenType.NUMERO':
        print(f'<NUMERO, "{k}"> ', end='')
    else:
        print(f'{v[0], v[1]} ', end='')
