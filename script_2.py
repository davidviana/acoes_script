from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

list_acoes = ['petr4', 'klbn11', 'mrfg3', 'jbss3', 'posi3']  # se você quiser colocar as ações predefinidas


def datacatch():
    for i in list_acoes:
        req = Request(f'https://statusinvest.com.br/acoes/{i}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req)
        complete_webpage = BeautifulSoup(webpage.read(), 'html5lib')
        pl_value = complete_webpage.find('strong', class_='value')
        print(f'{i.upper()}', '\nR$', pl_value.text, '\n')


datacatch()


def inputcatch():
    while True:
        acao = input("Digite uma ação: ").upper()
        req = Request(f'https://statusinvest.com.br/acoes/{acao}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req)
        complete_webpage = BeautifulSoup(webpage.read(), 'html5lib')
        pl_value = complete_webpage.find('strong', class_='value')
        print(f'{acao.upper()}', '\nR$', pl_value.text, '\n')


inputcatch()
