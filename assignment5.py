# url = "https://formy-project.herokuapp.com/form"
# fill the form details

import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)
driver.maximize_window()

url = "https://formy-project.herokuapp.com/form"

# get url

driver.get(url)
time.sleep(3)

first_name = driver.find_element(By.ID, "first-name")
time.sleep(2)
if first_name.is_displayed():
    time.sleep(2)
    first_name.send_keys("Hay")
    time.sleep(1)

last_name = driver.find_element(By.ID, "last-name")
time.sleep(2)
if last_name.is_displayed():
    last_name.send_keys("Day")
    time.sleep(2)

job_title = driver.find_element(By.ID, "job-title")
time.sleep(2)
if job_title.is_displayed():
    job_title.send_keys("N.A.")
    time.sleep(2)

highest_qualification = driver.find_element(By.ID, "radio-button-2")
time.sleep(2)
if not highest_qualification.is_selected():
    time.sleep(2)
    highest_qualification.click()
    time.sleep(2)

gender_applicant = driver.find_element(By.ID, "checkbox-1")
time.sleep(2)
if not gender_applicant.is_selected():
    time.sleep(2)
    gender_applicant.click()
    time.sleep(2)

dropdown_yoe = driver.find_element(By.ID, "select-menu")
select_yoe = Select(dropdown_yoe)
select_yoe.select_by_value("1")

# date
today = date.today()
date_in_mmddyy = today.strftime("m/%d/%y")
date_picker = driver.find_element(By.ID, "datepicker")
if date_picker.is_displayed():
    time.sleep(2)
    date_picker.click()
    time.sleep(3)
    select_today = driver.find_element(By.XPATH, "//td[@class='today day']")
    time.sleep(2)
    select_today.click()
    time.sleep(2)

click_submit = driver.find_element(By.XPATH, "//a[normalize-space()='Submit']")
time.sleep(2)
click_submit.click()
time.sleep(2)

driver.close()