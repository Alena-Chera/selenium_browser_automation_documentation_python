"""
https://www.selenium.dev/documentation/en/webdriver/browser_manipulation/

Frames and Iframes
"""

# To interact with the button on frames/iframes, we will need
# to
# 1. FIRST --> switch to the frame, in a similar way to how we switch windows.
#    WebDriver offers three ways of switching to a frame - Using a WebElement, Using a name or ID, Using an index

# a)
# Switching using a WebElement is the most flexible option.
# You can find the frame using your preferred selector and switch to it.

# Store iframe web element
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
iframe = driver.find_element(By.CSS_SELECTOR, "#modal > iframe")

# switch to selected iframe
driver.switch_to.frame(iframe)

# Now click on button
driver.find_element(By.TAG_NAME, 'button').click()

# b) Switching using a name or ID
# If your frame or iframe has an id or name attribute, this can be used instead.
# If the name or ID is not unique on the page, then the first one found will be switched to.

# Switch frame by id
driver.switch_to.frame('buttonframe')

# Now, Click on the button
driver.find_element(By.TAG_NAME, 'button').click()

# c) Switching using an index
# It is also possible to use the index of the frame,
# such as can be queried using window.frames in JavaScript.

# Switch to the second frame
driver.switch_to.frame(1)

# 2. SECOND --> Leaving a frame
# To leave an iframe or frameset, switch back to the default content like so:

# switch back to default content
driver.switch_to.default_content()
