"""
https://www.selenium.dev/documentation/en/webdriver/browser_manipulation/

Get window handle:
You can get the window handle of the current window by using this command
driver.current_window_handle
"""

"""
Switching windows or tabs:
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Start the driver
with webdriver.Chrome() as driver:
    # Open URL
    driver.get("https://www.scholastic.com/home")

    # Setup wait for later
    wait = WebDriverWait(driver, 10)

    # Store the ID of the original window
    original_window = driver.current_window_handle

    # Check we don't have other windows open already
    assert len(driver.window_handles) == 1

    # Click the link which opens in a new window
    driver.find_element(By.CSS_SELECTOR, "span.footer-link--privacy-policy__underline").click()

    # Wait for the new window or tab
    wait.until(EC.number_of_windows_to_be(2))

    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    # Wait for the new tab to finish loading content
    wait.until(EC.title_is("Privacy Policy | Scholastic Inc."))

    driver.delete_all_cookies()
    driver.quit()

"""
Create new window( or) new tab and switch:
"""
# Opens a new tab and switches to new tab
driver.switch_to.new_window('tab')

# Opens a new window and switches to new window
driver.switch_to.new_window('window')

"""
Closing a window or tab:
"""
# Close the tab or window
driver.close()

# Switch back to the old tab or window
driver.switch_to.window(original_window)

"""
Quitting the browser at the end of a session:
"""
driver.quit()


# Some test frameworks offer methods and annotations
# which you can hook into to tear down at the end of a test:
# unittest teardown
# https://docs.python.org/3/library/unittest.html?highlight=teardown#unittest.TestCase.tearDown
def tearDown(self):
    self.driver.quit()

# try / finally:
# If not running WebDriver in a test context,
# you may consider using try / finally which is offered by most languages
# so that an exception will still clean up the WebDriver session:

# try:
# # WebDriver code here...
# finally:
#     driver.quit()

# with keyword:
# Python’s WebDriver now supports the python context manager,
# which when using the with keyword can automatically quit the driver at the end of execution:
# with webdriver.Firefox() as driver:
#   # WebDriver code here...
# # WebDriver will automatically quit after indentation


