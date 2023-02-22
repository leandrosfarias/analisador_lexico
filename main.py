import re
from linguagem.auxiliares import operadores_aritmeticos,operadores_logicos,operadores_relacionais,operador_negacao,simbolos

tokens = {}

def leitura(path):
    return open(path).readlines()

saida = {}

arquivo = leitura('./testes/teste.txt')

def desmembra_progama(arquivo):
    programa = []
    for line in arquivo:
        line = line.strip().split(' ')
        programa.append(line)

    sem_espaco_em_branco = []

    for sentenca in programa:
        for exp in sentenca:
            sem_espaco_em_branco.append(exp)

    separacao_simbolos = []

    for elemento in sem_espaco_em_branco:
        if len(elemento) > 1 and elemento != ':=':
            for caracter in elemento:
                if caracter in simbolos:
                    index = sem_espaco_em_branco.index(elemento)
                    aux = re.split('([;().:,])', sem_espaco_em_branco[sem_espaco_em_branco.index(elemento)])
                    aux = list(filter(None, aux))
                    sem_espaco_em_branco.remove(elemento)
                    for elemt in range(len(aux)):
                        sem_espaco_em_branco.insert(index+elemt, aux[elemt])
                    break
    separacao_simbolos = sem_espaco_em_branco

    remove_comentarios  = []

    for elemento in separacao_simbolos:
        if not elemento.startswith('//'):
            remove_comentarios.append(elemento)

    return print(remove_comentarios)


desmembra_progama(arquivo)
