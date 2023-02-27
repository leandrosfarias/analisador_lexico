import re
from linguagem.Gramatica import Gramatica
from scanner.Scanner import Scanner

if __name__ == '__main__':
    programa = Scanner('./teste.txt')
    g = Gramatica().une_regras()
    for l in programa.programa:
        print(re.findall(g, l))
