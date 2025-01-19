from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)
driver.maximize_window()

url = "https://rahulshettyacademy.com/AutomationPractice/"

# get url

driver.get(url)

# for dropdown selection we have select class
# select by visible text
# select by value
# select by index

dropdown = driver.find_element(By.ID, 'dropdown-class-example')
sel = Select(dropdown)

# select by visible text

time.sleep(5)

sel.select_by_visible_text("Option1")

# select by value text

time.sleep(5)
sel.select_by_value("option3")

# select by index number

time.sleep(5)
sel.select_by_index(2)

time.sleep(2)
driver.close()

