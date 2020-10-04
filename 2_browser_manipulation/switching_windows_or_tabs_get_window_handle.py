"""
Windows and tabs: https://www.selenium.dev/documentation/en/webdriver/browser_manipulation/

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