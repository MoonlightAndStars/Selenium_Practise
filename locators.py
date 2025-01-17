import time

from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)
driver.maximize_window()


driver.get("https://rahulshettyacademy.com/angularpractice/")

time.sleep(2)

# find element - used to indentify single element
# find elements - used to identify more than one element.

# name locator
username = driver.find_element(By.NAME, "name")
username.send_keys("Hayat")

# email

email = driver.find_element(By.NAME, "email")
email.send_keys("hayat@abc.com")

# password

password = driver.find_element(By.ID, "exampleInputPassword1")
password.send_keys("hhh78a6er2")

# xpath

submit = driver.find_element(By.XPATH, "//input[@value='Submit']")
submit.click()