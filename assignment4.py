# url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"
# add customer, open account, check customer.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)
driver.maximize_window()

url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"

# get to the url

driver.get(url)
time.sleep(4)
# go to the add customer button

click_add_customer = driver.find_element(By.XPATH, "//button[normalize-space()='Add Customer']")
click_add_customer.click()
time.sleep(4)

# adding customer details

adding_first_name = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
first_name = input("Enter first name : ")
adding_first_name.send_keys(first_name)
time.sleep(3)

adding_last_name = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
last_name = input("Enter last name : ")
adding_last_name.send_keys(last_name)
time.sleep(5)

adding_post_code = driver.find_element(By.XPATH, "//input[@placeholder='Post Code']")
pin_code = input("Enter Pincode : ")
adding_post_code.send_keys(pin_code)
time.sleep(3)

# clicking the submit button

submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
if submit_button.is_enabled():
    submit_button.click()

time.sleep(2)

# full name
full_name = first_name + " " + last_name
# alt = driver.switch_to.alert
# alt.accept()

time.sleep(2)
open_account = driver.find_element(By.XPATH, "//button[normalize-space()='Open Account']")
open_account.click()
time.sleep(2)

# select the account that was created

username_dropdown = driver.find_element(By.XPATH, "//select[@id='userSelect']")
time.sleep(2)
select_user = Select(username_dropdown)
select_user.select_by_visible_text(full_name)
time.sleep(3)
currency_dropdown = driver.find_element(By.XPATH, "//select[@id='currency']")
time.sleep(2)
currency_select = Select(currency_dropdown)
currency_select.select_by_value("Rupee")
time.sleep(3)

# click on process

button_click = driver.find_element(By.XPATH, "//button[normalize-space()='Process']")
time.sleep(3)
button_click.click()

time.sleep(3)

# clicking customers tab

customers_tab = driver.find_element(By.XPATH, "//button[normalize-space()='Customers']")
customers_tab.click()
time.sleep(3)

# SEARCH customer

search_customer = driver.find_element(By.XPATH, "//input[@placeholder='Search Customer']")
time.sleep(3)

search_customer.send_keys(full_name)
time.sleep(3)
if search_customer.is_displayed():
    time.sleep(3)
    print("Customer Present")
else:
    print("No such customer exist.")