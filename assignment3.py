import time
from selenium import webdriver
from selenium.webdriver.common.by import By


option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)
driver.maximize_window()

url = "http://seleniumpractise.blogspot.com/"

# get url
driver.get(url)

# boxes ticked
elements = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
count = len(elements)

for i in range(count):
    time.sleep(3)
    elements[i].click()
    if elements[i].is_selected():
        print(f"Element {elements[i]} got selected.")
    else:
        print(f"Element is not displayed.")

# moving to different websites

google = driver.find_element(By.LINK_TEXT, "Google")
facebook = driver.find_element(By.LINK_TEXT, "Facebook")
yahoo = driver.find_element(By.LINK_TEXT, "Yahoo")

websites = [google, facebook, yahoo]

for website in websites:
    if website.is_displayed():
        website.click()
        time.sleep(5)
        driver.back()
        print(f"Clicked {website}")
