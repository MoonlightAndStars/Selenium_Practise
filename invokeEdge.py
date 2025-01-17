from selenium import webdriver

option = webdriver.EdgeOptions()
driver = webdriver.Edge(options = option)
driver.maximize_window()
driver.get('https://www.indiarailinfo.com')

