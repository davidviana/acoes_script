import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
from script_2 import openbrowser


def system():
    # openbrowser()

    # coleta de dados
    page = urllib.request.urlopen("https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil_por_%C3%A1rea")
    soup = BeautifulSoup(page.read(), 'html5lib')
    table_sorted = soup.find('table', class_='wikitable sortable')

    # definindo as colunas
    A = []
    B = []
    C = []
    D = []
    E = []

    # captando os dados para as linhas e colunas
    for row in table_sorted.findAll("tr"):
        cells = row.findAll('td')
        if len(cells) == 5:
            A.append(cells[0].find(text=True))
            B.append(cells[1].find(text=True))
            C.append(cells[2].find(text=True))
            D.append(cells[3].find('a').text)
            E.append(cells[4].find(text=True))

    # adição na planilha
    df = pd.DataFrame(index=A)

    df['Id'] = A
    df['Capital'] = B
    df['Semana'] = C
    df['Estados'] = D
    df['Renda'] = E

    # converter em arquivo de excel

    writer = pd.ExcelWriter("cotação-de-ações.xlsx")
    df.to_excel(writer)
    writer.save()
    print('A planilha foi criada com sucesso')


system()

# TODO
# acessar o link https://www.investsite.com.br/seleciona_acoes.php
# pegar a cotação das ações
# gerar uma planilha => FUTURO: manipular uma planilha já existente
# criação de filtro
# aplicação de filtros
# comparação com o periodo anterior
# Criar uma execução recorrente
