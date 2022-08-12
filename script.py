from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# coleta de dados
page = urlopen("https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil_por_%C3%A1rea")
soup = BeautifulSoup(page.read(), 'html5lib')
all_table = soup.find_all('table')
table_sorted = soup.find('table', class_='wikitable sortable')

# definindo as colunas
A = []
B = []
C = []
D = []
E = []
# F = []
# G = []
# H = []

# captando os dados para as linhas e colunas
for row in table_sorted.findAll("tr"):  # para tudo que estiver em <tr>
    cells = row.findAll('td')  # variável para encontrar <td>
    if len(cells) == 5:  # número de colunas
        A.append(cells[0].find(text=True))  # iterando sobre cada linha
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find('a').text)
        E.append(cells[4].find(text=True))

# adição na planilha
df = pd.DataFrame(index=A)

df['Ação'] = A
df['Empresa'] = B
df['Preço'] = C
df['Margem EBIT'] = D
df['EV/EBIT'] = E
# df['Volume Financ.(R$)'] = F
# df['Quantidade de Ações'] = G
# df['Total Investido'] = H

# converter em arquivo de excel

writer = pd.ExcelWriter("converted-to-excel.xlsx")
df.to_excel(writer)
writer.save()
print('A planilha foi criada com sucesso')
