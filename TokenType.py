from enum import Enum


class TokenType(Enum):
    ID = 0
    NUMERO = 1
    OPAD = 2
    OPMULT = 3
    OPLOG = 4
    OPNEG = 5
    OPREL = 6
    PVIG = 7
    PONTO = 8
    DPONTOS = 9
    VIG = 10
    ABPAR = 11
    FPAR = 12
    ATRIB = 13
    # PONTUACAO = 4
    # ATRIBUICAO = 4
    # PALAVRA_RESERVADA = 5
