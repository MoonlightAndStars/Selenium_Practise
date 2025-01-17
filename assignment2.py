# login the website, select product, add to cart, do check out by entering name address pincode.


from selenium import webdriver
import time
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

time.sleep(3)

# login functionality

username = driver.find_element(By.ID, "user-name")
username.send_keys("performance_glitch_user")

password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

time.sleep(2)

login = driver.find_element(By.ID, "login-button")
login.click()

time.sleep(1)
# select items from page

select_bag = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
select_bag.click()

time.sleep(1)

select_tshirt = driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
select_tshirt.click()

time.sleep(1)

select_jacket = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
select_jacket.click()

time.sleep(1)

# go to cart functionality

cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart.click()

time.sleep(3)

# checkout functionality

checkout_click = driver.find_element(By.ID, "checkout")
checkout_click.click()

time.sleep(2)

# enter checkout details

firstname = driver.find_element(By.ID, "first-name")
firstname.send_keys("Godzilla")

time.sleep(1)

lastname = driver.find_element(By.ID, "last-name")
lastname.send_keys("Python")

time.sleep(1)
zip_code = driver.find_element(By.ID, "postal-code")
zip_code.send_keys("110110")

time.sleep(1)
contnue_button = driver.find_element(By.ID, "continue")
contnue_button.click()

time.sleep(3)

# click finish
click_finish = driver.find_element(By.ID,"finish")
click_finish.click()
time.sleep(2)
driver.quit()