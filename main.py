from Scanner import Scanner
from Token import Token
from TokenType import TokenType
from auxiliares import is_space, is_operator, check_palavra_reservada, \
    operadores_aritmeticos, operadores_logicos, \
    operador_negacao, operadores_relacionais, simbolos

scanner = Scanner('teste.txt')
estado = 0
termo = ''
token = None
tokens = {}
current_char = ''

while scanner.has_next():
    # print(scanner.read_char())
    current_char = scanner.read_char().upper()
    # termo = current_char
    match estado:
        case 0:
            if current_char.isalpha():
                termo += current_char
                # faz a transição para q1
                estado = 1
                continue
            # if check_palavra_reservada(termo):
            #     token = Token(TokenType.PALAVRA_RESERVADA)
            if current_char.isdigit():
                termo += current_char
                estado = 3
            if is_space(current_char):
                pass
            if current_char == '\n' or current_char == '\t':
                pass
            if is_operator(current_char):
                termo += current_char
                estado = 5
                continue
                # if current_char in operadores_aritmeticos:
                #     if current_char in ['+', '-']:
                #         if current_char == '+':
                #             token = Token(TokenType.OPAD, 'MAIS')
                #             tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
                #             termo = ''
                #         else:
                #             token = Token(TokenType.OPAD, 'MENOS')
                #             tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
                #             termo = ''
                #     elif current_char in ['*', '/']:
                #         if current_char == '*':
                #             token = Token(TokenType.OPMULT, 'VEZES')
                #             tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
                #         else:
                #             token = Token(TokenType.OPMULT, 'DIV')
                #             tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
                # elif current_char in operadores_logicos:
                #     if current_char in ['OR', 'AND']:
                #         if current_char == 'OR':
                #             token = Token(TokenType.OPLOG, 'OR')
                #             tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
                #         else:
                #             token = Token(TokenType.OPLOG, 'AND')
                #             tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
                # elif current_char == operador_negacao:
                #     token = Token(TokenType.OPNEG, '~')
                # elif current_char in operadores_relacionais:
                #     if current_char == '<':
                #         token = Token(TokenType.OPREL, 'MENOR')
                #         tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
                #     elif current_char == '<=':
                #         token = Token(TokenType.OPREL, 'MENIG')
                #         tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
                #     elif current_char == '>':
                #         token = Token(TokenType.OPREL, 'MAIOR')
                #         tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
                #     elif current_char == '>=':
                #         token = Token(TokenType.OPREL, 'MAIG')
                #         tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
                #     elif current_char == '==':
                #         token = Token(TokenType.OPREL, 'IGUAL')
                #         tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
                #     elif current_char == '<>':
                #         token = Token(TokenType.OPREL, 'DIFER')
                #         tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
                # elif current_char in simbolos:
                #     if current_char == ';':
                #         token = Token(TokenType.PVIG, '')
                #         tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
                #     elif current_char == '.':
                #         token = Token(TokenType.PONTO, '')
                #         tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
                #     elif current_char == ':':
                #         token = Token(TokenType.DPONTOS, '')
                #         tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
                #     elif current_char == ',':
                #         token = Token(TokenType.VIG, '')
                #         tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
                #     elif current_char == '(':
                #         token = Token(TokenType.ABPAR, '')
                #         tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
                #     elif current_char == ')':
                #         token = Token(TokenType.FPAR, '')
                #         tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
                #     elif current_char == ':=':
                #         token = Token(TokenType.ATRIB, '')
                #         tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
                # estado = 5
        case 1:
            # if is_space(current_char):
            #     continue
            if current_char.isalpha() or current_char.isdigit():
                termo += current_char
                estado = 1
                continue
            if is_space(current_char) or is_operator(current_char):
                # estado = 0
                if is_operator(current_char):
                    if check_palavra_reservada(termo):
                        estado = 5
                        token = Token(termo)
                        tokens[f'{termo}'] = (f'{termo}', '')
                        termo = current_char
                    else:
                        estado = 5
                        token = Token(TokenType.ID)
                        tokens[f'{termo}'] = (f'{TokenType.ID}', f'{termo}')
                        termo = current_char
                    continue

                if check_palavra_reservada(termo):
                    estado = 0
                    token = Token(termo)
                    tokens[f'{termo}'] = (f'{termo}', '')
                    termo = current_char
                else:
                    estado = 0
                    token = Token(TokenType.ID)
                    tokens[f'{termo}'] = (f'{TokenType.ID}', f'{termo}')
                    termo = current_char
                continue
        case 2:
            # estado = 0
            # if current_char.isalpha():
            #     estado = 0
            if check_palavra_reservada(termo):
                token = Token(termo)
                tokens[f'{termo}'] = (f'{termo}', '')
                # Volta para estado inicial
                # estado = 0
            else:
                token = Token(TokenType.ID)
                # Volta para estado inicial
                # estado = 0
        case 3:
            if current_char.isdigit():
                termo += current_char
                estado = 3
            if is_space(current_char) or is_operator(current_char) or current_char == '\n' or current_char == '':
                estado = 4
                token = Token(TokenType.NUMERO)
                continue
        case 4:
            token = Token(TokenType.NUMERO)
        case 5:
            # if is_space(current_char):
            #     estado = 0
            #     continue
            if termo.strip() in simbolos:
                if termo.strip() == ';':
                    token = Token(TokenType.PVIG, '')
                    tokens[f'{termo.strip()}'] = (f'{token.tipo}', f'{token.atributo}')
                elif termo.strip() == '.':
                    token = Token(TokenType.PONTO, '')
                    tokens[f'{termo.strip()}'] = (f'{token.tipo}', f'{token.atributo}')
                elif termo.strip() == ':':
                    token = Token(TokenType.DPONTOS, '')
                    tokens[f'{termo.strip()}'] = (f'{token.tipo}', f'{token.atributo}')
                elif termo.strip() == ',':
                    token = Token(TokenType.VIG, '')
                    tokens[f'{termo.strip()}'] = (f'{token.tipo}', f'{token.atributo}')
                elif termo.strip() == '(':
                    token = Token(TokenType.ABPAR, '')
                    tokens[f'{termo.strip()}'] = (f'{token.tipo}', f'{token.atributo}')
                elif termo.strip() == ')':
                    token = Token(TokenType.FPAR, '')
                    tokens[f'{termo.strip()}'] = (f'{token.tipo}', f'{token.atributo}')
                elif termo.strip() == ':=':
                    token = Token(TokenType.ATRIB, '')
                    tokens[f'{termo.strip()}'] = (f'{token.tipo}', f'{token.atributo}')
            elif termo.strip() in operadores_aritmeticos:
                if termo.strip() in ['+', '-']:
                    if termo == '+':
                        token = Token(TokenType.OPAD, 'MAIS')
                        tokens[f'{termo.strip()}'] = (f'{token.tipo}', f'{token.atributo}')
                    else:
                        token = Token(TokenType.OPAD, 'MENOS')
                        tokens[f'{termo.strip()}'] = (f'{token.tipo}', f'{token.atributo}')
                elif termo.strip() in ['*', '/']:
                    if termo.strip() == '*':
                        token = Token(TokenType.OPMULT, 'VEZES')
                        tokens[f'{termo.strip()}'] = (f'{token.tipo}', f'{token.atributo}')
                    else:
                        token = Token(TokenType.OPMULT, 'DIV')
                        tokens[f'{termo.strip()}'] = (f'{token.tipo}', f'{token.atributo}')
            elif termo in operadores_logicos:
                if termo in ['OR', 'AND']:
                    if termo == 'OR':
                        token = Token(TokenType.OPLOG, 'OR')
                        tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
                    else:
                        token = Token(TokenType.OPLOG, 'AND')
                        tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
            elif termo == operador_negacao:
                token = Token(TokenType.OPNEG, '~')
            elif termo in operadores_relacionais:
                if current_char == '<':
                    token = Token(TokenType.OPREL, 'MENOR')
                    tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
                elif termo == '<=':
                    token = Token(TokenType.OPREL, 'MENIG')
                    tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
                elif termo == '>':
                    token = Token(TokenType.OPREL, 'MAIOR')
                    tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
                elif termo == '>=':
                    token = Token(TokenType.OPREL, 'MAIG')
                    tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
                elif termo == '==':
                    token = Token(TokenType.OPREL, 'IGUAL')
                    tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
                elif termo == '<>':
                    token = Token(TokenType.OPREL, 'DIFER')
                    tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')
            if is_space(current_char):
                estado = 0
                termo = ''
                continue

if current_char == ';':
    token = Token(TokenType.PVIG, '')
    tokens[f'{termo}'] = (f'{token.tipo}', f'{token.atributo}')


scanner.close()
# print(f'Ultimo estado: {estado}')
# print(f'Termo: {termo}')
# print(f'Tipo do token: {token.tipo}')
# for k, v in tokens.items():
#     print(f'Token: {k}: Tipo: {v}')

for v in tokens.values():
    # if v[0] == TokenType.ID:
    #     print(f'<IDENTIFICADOR,{v[1]}> ', end='')
    if v[0] == 'TokenType.ID':
        print(f'<identificador, "{v[1]}"> ', end='')
    elif v[0] == 'TokenType.OPAD' and v[1] == 'MENOS':
        print(f'<SUBTRACAO> ', end='')
    elif v[0] == 'TokenType.PVIG':
        print(f'<PONTOVIRGULA> ')
    else:
        print(f'{v[0], v[1]} ', end='')
