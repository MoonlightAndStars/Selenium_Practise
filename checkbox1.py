import time
from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)
driver.maximize_window()

url = "https://rahulshettyacademy.com/AutomationPractice/"

driver.get(url)

time.sleep(1)

# multiple select options
checkbox_list = driver.find_elements(By.XPATH, "//*[@type='checkbox']")
count = len(checkbox_list)
print(count)

time.sleep(1)

for i in checkbox_list:
    time.sleep(2)
    i.click()

time.sleep(2)

driver.close()