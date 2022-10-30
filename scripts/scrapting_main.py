from scrapting import CollectWeb


def mostrarClubes():
    while True:
        try:
            collect = CollectWeb(
                'https://www.gazetaesportiva.com/campeonatos/brasileiro-serie-a/')
            collect.mostrarTitulo('tr', 'table__green')
            break
        except Exception as error:
            print(error)
            break


mostrarClubes()
