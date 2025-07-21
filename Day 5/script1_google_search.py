from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open Google
driver.get("https://www.google.com")
print("Opened Google Homepage")

# Locate search box and search for QA Testing
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("QA Testing")
search_box.send_keys(Keys.RETURN)

# Wait and print page title
time.sleep(2)
print("Search Results Page Title:", driver.title)

# Close browser
driver.quit()