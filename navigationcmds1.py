from selenium import webdriver
import time

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Navigational Commands
#navigation back

time.sleep(2)
driver.back()

# navigate forward
time.sleep(2)
driver.forward()

# page refresh
time.sleep(2)
driver.refresh()

time.sleep(2)
driver.close()