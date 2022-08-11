from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


#Coleta de dados

page = urlopen("https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil")
soup = BeautifulSoup(page.read(), 'html5lib')
list_item = soup.find('title').text
print(list_item)
name = (list_item).strip()
print("name: ", name)

#Colunas
A = []
B = []
C = []
D = []
E = []
F = []
G = []
H = []


#Adição na planilha
df = pd.DataFrame(index=A, columns=['Posição'])

df['Ação']=A
df['Empresa']=B
df['Preço']=C
df['Margem EBIT']=D
df['EV/EBIT']= E
df['Volume Financ.(R$)']=F
df['Quantidade de Ações']=G
df['Total Investido']=H
