import re

class Scanner():

    def __init__(self, caminho):
        self.programa = open(caminho).readlines()
        self.trata_programa()


    def trata_programa(self):
        for linha in self.programa:
            if '//' in linha:
                comentario_tratado = re.sub(r"\/\/.*(?:\r?|$)", "", linha)
                if comentario_tratado != '':
                    self.programa[self.programa.index(linha)] = comentario_tratado
        if '\n' in self.programa:
            self.programa.remove('\n')
        for linha in self.programa:
            self.programa[self.programa.index(linha)] = linha.replace(" ", '')
