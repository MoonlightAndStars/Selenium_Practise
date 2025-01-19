import time
from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)
driver.maximize_window()

url = "http://seleniumpractise.blogspot.com/"

# get url
driver.get(url)

element = driver.find_element(By.LINK_TEXT, "Facebook")
if element.is_displayed():
    element.click()
    print("Element is Clicked")
else:
    print("Element is not clicked !")
