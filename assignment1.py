from selenium import webdriver
import time

from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.maximize_window()

url = "https://opensource-demo.orangehrmlive.com/"

# get to the url

driver.get(url)

# login

time.sleep(2)
# for username

username = driver.find_element(By.NAME, "username")
username.send_keys("Admin")
time.sleep(3)

# for password

password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")

# for submit button

time.sleep(3)

submit = driver.find_element(By.XPATH, "//button[@type='submit']")
submit.click()
time.sleep(3)
# clicking the admin option after logging in
# selecting admin

admin_select = driver.find_element(By.LINK_TEXT, "Admin")
admin_select.click()
time.sleep(5)
# selecting the checkboxes one by one

checkbox_list = driver.find_elements(By.XPATH, "//i[@class = 'oxd-icon bi-check oxd-checkbox-input-icon']")
count = len(checkbox_list)
print(count)
time.sleep(4)

for i in range(3,count+1):
    checkbox_list[i].click()
    time.sleep(3)

time.sleep(3)

driver.close()
