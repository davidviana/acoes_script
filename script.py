from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time


def init_system():
    # openbrowser()
    datacatch()


def datacatch():
    # coleta de dados
    url = Request("https://br.investing.com/equities/", headers={'User-Agent': 'Mozilla/5.0'})
    opened_page = urlopen(url)
    webpage = BeautifulSoup(opened_page.read(), 'html5lib')
    table_sorted = webpage.find('table', class_='genTbl closedTbl crossRatesTbl elpTbl elp30')

    # definindo as colunas
    A = []
    B = []
    C = []
    D = []
    E = []
    F = []
    G = []
    H = []

    # captando os dados para as linhas e colunas
    for row in table_sorted.findAll("tr"):
        cells = row.find_all('td')
        if len(cells) == 10:
            A.append(cells[1].find(text=True))
            B.append(cells[2].find(text=True))
            C.append(cells[3].find(text=True))
            D.append(cells[4].find(text=True))
            E.append(cells[5].find(text=True))
            F.append(cells[6].find(text=True))
            G.append(cells[7].find(text=True))
            H.append(cells[8].find(text=True))

    # adição na planilha
    df = pd.DataFrame(index=A)
    df['Nome'] = A
    df['Ultimo'] = B
    df['Maximo'] = C
    df['Minimo'] = D
    df['Variação'] = E
    df['Var %'] = F
    df['Vol'] = G
    df['Hora'] = H

    # converter em arquivo de excel

    writer = pd.ExcelWriter("cotação-de-ações.xlsx")
    df.to_excel(writer)
    writer.save()
    print('A planilha foi criada com sucesso')


def openbrowser():
    driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    driver.get('https://www.investsite.com.br/seleciona_acoes.php')
    driver.maximize_window()

    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/form/input[2]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/form/table/tbody/tr[8]/td[4]/input').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/form/table/tbody/tr[21]/td[4]/input').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/form/table/tbody/tr[24]/td[4]/input').click()
    time.sleep(5)

    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/form/input[1]').click()


while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time == current_time or '07:40:00':
        init_system()
        break
    else:
        continue

# TODO
# acessar o link https://www.investsite.com.br/seleciona_acoes.php
# pegar a cotação das ações
# gerar uma planilha => FUTURO: manipular uma planilha já existente
# criação de filtro
# aplicação de filtros
# comparação com o periodo anterior
# Criar uma execução recorrente
