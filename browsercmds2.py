from selenium import webdriver

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)
driver.maximize_window()

url = "https://www.amazon.in/"
# 1- get the URL - get()
driver.get(url)

# 2 - getTitle - to get the title of the URL loaded.
title = driver.title
print(title)

# 3 - getCurrentURL - to get the current URL
current_url = driver.current_url
print(current_url)

# 4 - getPageSource() - gets page source return the html code of webpage

page_source = driver.page_source
print(page_source)

# 5 - close() - to close the current window

driver.close()

# 6 - quit() - to quit all the browser window

# driver.quit()