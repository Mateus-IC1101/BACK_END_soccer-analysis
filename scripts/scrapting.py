# .prettify()
import requests
from bs4 import BeautifulSoup


class CollectWeb:
    def __init__(self, url):
        self.page = url

    # -> MÉTODOS PÚBLICOS ABAIXO
    def mostrarTitulo(self, tag="", classe="", tag_sub=""):
        if not tag:
            print('Ops! Tag não inserida\n')
            return

        html = requests.get(self.page)
        soup = BeautifulSoup(html.text, 'html.parser')

        clubes = soup.find_all(tag, attrs={'class': classe})
        pontos = soup.find_all('td', attrs={'class': 'table__stats'})

        self.__percorrerClubes(clubes, pontos)

    # -> MÉTODOS PRIVADOS ABAIXO
    def __percorrerPontos(self, colecao):
        quant = 1
        for i in colecao:
            print(25 * '-', quant, 25 * ' -')
            print(i.prettify())
            quant += 1

    def __percorrerClubes(self, colecao, pontos):

        # quantidade de clubes
        clubes = [[] for _ in range(20)]
        # índice do clube a cada ciclo de 9 informações pertencentes a cada um.
        posicao_clube = 0
        # ciclo de cada informação
        ciclo = 0

        for i in pontos:
            if ciclo == 9:
                posicao_clube += 1
                ciclo = 0
            clubes[posicao_clube].append(i.text)
            ciclo += 1
        print(clubes)
