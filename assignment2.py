# select selenium and cucumber
#  url = http://seleniumpractise.blogspot.com/

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)
driver.maximize_window()

url = "http://seleniumpractise.blogspot.com/"

# get url
driver.get(url)

time.sleep(3)
# select dropdown
dropdown1 = driver.find_element(By.ID, "tools")
sel = Select(dropdown1)

dropdown2 = driver.find_element(By.ID, "tools1")
sel2 = Select(dropdown2)

# select selenium from dropdown 1
time.sleep(5)
sel.select_by_value("Selenium")
time.sleep(5)
sel2.select_by_visible_text("Cucumber")
time.sleep(5)

# trying index in 1 dropdown (additional)
sel.select_by_index(2)
time.sleep(2)

driver.close()

