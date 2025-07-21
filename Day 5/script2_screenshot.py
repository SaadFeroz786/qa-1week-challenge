from selenium import webdriver
import time

# Setup WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to Example website
driver.get("https://example.com")
time.sleep(2)

# Save screenshot
driver.save_screenshot("example_screenshot.png")
print("Screenshot saved as example_screenshot.png")

# Close browser
driver.quit()
