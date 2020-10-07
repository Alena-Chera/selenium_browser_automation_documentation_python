"""
https://www.selenium.dev/documentation/en/webdriver/js_alerts_prompts_and_confirmations/

 JavaScript alerts, prompts and confirmations.
 WebDriver provides an API for working with the three types of native popup messages offered by JavaScript.
 These popups are styled by the browser and offer limited customisation.

                       JavaScript prompts:
                       Prompts are similar to confirm boxes,
                       except they also include a text input.
                       Similar to working with form elements,
                       you can use WebDriver’s send keys to fill in a response.
                       This will completely replace the placeholder text.
                       Pressing the cancel button will not submit any text.
 See a sample prompt
"""
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Firefox

# Click the link to activate the alert
driver.find_element(By.LINK_TEXT, "See a sample prompt").click()

# Wait for the alert to be displayed
wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.alert_is_present())

# Store the alert in a variable for reuse
alert = Alert(driver)

# Type your message
alert.send_keys("Selenium")

# Press the OK button
alert.accept()
