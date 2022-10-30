# .prettify()
import requests
from bs4 import BeautifulSoup


class CollectWeb:
    def __init__(self, url):
        self.page = url
        self.clubes = {}

    # -> MÉTODOS PÚBLICOS ABAIXO
    def mostrarClubes(self, tag="", classe="",):
        if not tag:
            print('Ops! Tag não inserida\n')
            return

        html = requests.get(self.page)
        soup = BeautifulSoup(html.text, 'html.parser')

        clubes_atuais = soup.find_all(tag, attrs={'class': classe})
        pontos_atuais = soup.find_all('td', attrs={'class': 'table__stats'})

        self.__percorrerClubes(clubes_atuais,  pontos_atuais)

    # -> MÉTODOS PRIVADOS ABAIXO
    def __percorrerPontos(self, colecao):
        quant = 1
        for i in colecao:
            print(25 * '-', quant, 25 * ' -')
            print(i.prettify())
            quant += 1

    def __percorrerClubes(self, colecao, pontos):
        """
        (self.clubes) é quantidade de clubes para facilitar o uso de manipulações nas funções. Desse modo, não é 
        necessário realizar a instancia de uma variável global para cada função.
        """
        self.clubes = [[] for _ in range(20)]
        """
        (clubes_dict) irá conter como chave o nome dos clubes e nos valores de cada índice conterá um array com os
        pontos por cada critério.
        """
        clubes_dict = {}
        # índice do clube a cada ciclo de 9 informações pertencentes a cada um. 9 = quantidades de items do site.

        posicao_clube = 0
        # ciclo de cada informação
        ciclo = 0

        for i in pontos:
            if ciclo == 9:
                posicao_clube += 1
                ciclo = 0
            self.clubes[posicao_clube].append(i.text)
            ciclo += 1

        for index, i in enumerate(colecao):
            # print(type(self.clubes[i]))
            clubes_dict.update({i.text: self.clubes[index]})
        for k, v in clubes_dict.items():
            print(k, '=>', v)
