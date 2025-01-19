# url = https://grotechminds.com/multiple-select/

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)
driver.maximize_window()

url = "https://grotechminds.com/multiple-select/"

# get url

driver.get(url)
time.sleep(5)

# select from window

menu = driver.find_element(By.ID, "automobiles")
sel = Select(menu)
time.sleep(2)
sel.select_by_value("motorcycle")
time.sleep(3)
sel.select_by_index(2)
time.sleep(3)
sel.select_by_visible_text("Sedan")
time.sleep(3)
sel.select_by_value("suv")
time.sleep(3)
sel.deselect_by_visible_text("Motorcycle")
time.sleep(3)
sel.deselect_by_value("sedan")
time.sleep(3)
sel.deselect_by_index(2)
time.sleep(2)
sel.deselect_by_visible_text("SUV")
time.sleep(3)


button_for_all = driver.find_element(By.XPATH, "//input[@value='Select/Deselect All']")
time.sleep(2)
button_for_all.click()
time.sleep(3)
button_for_all.click()
time.sleep(2)
print("All the buttons have been selected and deselected one by one and all at once.")
driver.close()

# trying for loop in this // //option[@value='motorcycle']

# path = ["//option[@value='motorcycle']", "//option[@value='motorcycle']", "//option[@value='motorcycle']", "//option[@value='motorcycle']" ]

