from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
driver.refresh()
chk = driver.find_elements_by_xpath("//input[@type='radio']")
print(len(chk))
for i in chk:
    if i.get_attribute("value") == "Male":
        i.click()
        driver.close()
