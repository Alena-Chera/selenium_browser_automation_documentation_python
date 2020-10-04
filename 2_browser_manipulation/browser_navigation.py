"""
Browser navigation:
https://www.selenium.dev/documentation/en/webdriver/browser_manipulation/

"""

from selenium import webdriver

driver = webdriver.Firefox()

# Navigate to
driver.get("https://selenium.dev")

# Get current URL
driver.current_url

# Back
driver.back()

# Forward
driver.forward()

# Refresh
driver.refresh()

# Get title
driver.title

