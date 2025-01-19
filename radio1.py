import time
from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)
driver.maximize_window()

url = "https://rahulshettyacademy.com/AutomationPractice/"

driver.get(url)

# selecting radio button

radio_1 = driver.find_element(By.XPATH, "//*[@id='radio-btn-example']/fieldset/label[3]/input")
radio_1.click()

time.sleep(2)

# dropdown menu

dropdown = driver.find_element(By.ID, "dropdown-class-example")
dropdown.click()

time.sleep(2)

option3 = driver.find_element(By.XPATH, "//*[@id='dropdown-class-example']/option[4]")
option3.click()

time.sleep(2)

# checkbox

checkbox = driver.find_element(By.XPATH, "//*[@id='checkBoxOption3']")
checkbox.click()
time.sleep(3)

# another way - this is the concept of indexing and here index starts from 1

another_way = driver.find_element(By.XPATH, "(//*[@type='checkbox'])[2]")
another_way.click()
time.sleep(3)
driver.close()