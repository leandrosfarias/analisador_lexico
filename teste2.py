from Scanner import Scanner
import re
from TokenType import TokenType

scanner = Scanner('teste.txt')
estado = 0
termo = ''
# token = None
tokens = {}

current_char = ''


def tokenize(termo: str, tipo, atributo=''):
    tokens[f'{termo}'] = (f'{tipo}', f'{atributo}')


while scanner.has_next():
    current_char = scanner.read_char().upper()
    match estado:
        # estado inicial q0
        case 0:
            # Se lê alguma letra
            if re.match(r'[A-Z]', current_char):
                # transição para q1
                estado = 1
                # começa a montar o termo com o primeiro caracter
                termo += current_char
                # vai para proxima iteração, consequentemente, atualizando current_char com o próximo caractere
                continue
        case 1:
            # qualquer letra ou número, permanece em loop
            if re.match(r'[A-Z\d]', current_char):
                # continua montando o termo
                termo += current_char
            # caso leia qualquer outro tipo de caracter, espaço ou símbolos especiais
            # faz transição para q2, estado de aceitação
            else:
                estado = 2
                continue
        # q2 estado de aceite, retorna o termo tokenizado
        case 2:
            # Verificar se é identificador ou palavra reservada
            # Se for palavra reservada
            if re.match(r'PROGRAM|INTEGER|BOOLEAN|BEGIN|END|WHILE|DO|READ|VAR|FALSE|TRUE|WRITE', termo):
                tokenize(termo, termo)
            else:
                tokenize(termo, TokenType.ID)
            estado = 0
            continue

for k, v in tokens.items():
    print(f'{k} -> {v}')
