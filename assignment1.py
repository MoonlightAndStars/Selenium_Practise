# login scenario of orange hrm

# https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(2)
# for username

username = driver.find_element(By.NAME, "username")
username.send_keys("Admin")


# for password

password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")

# for submit button

time.sleep(2)

submit = driver.find_element(By.XPATH, "//button[@type='submit']")
submit.click()
time.sleep(2)
driver.quit()