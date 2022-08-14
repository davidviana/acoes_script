from selenium import webdriver


def openbrowser():
    driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    page = 'https://br.investing.com/equities/'
    driver.get(page)

