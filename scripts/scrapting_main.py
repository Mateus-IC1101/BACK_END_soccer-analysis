from scrapting import CollectWeb


def run():
    while True:
        try:
            collect = CollectWeb(
                'https://www.gazetaesportiva.com/campeonatos/brasileiro-serie-a/')
            collect.mostrarClubes('td', 'table__team')
            break
        except Exception as error:
            print(error)
            break


run()
