"""
https://www.selenium.dev/documentation/en/webdriver/js_alerts_prompts_and_confirmations/

 JavaScript alerts, prompts and confirmations.
 WebDriver provides an API for working with the three types of native popup messages offered by JavaScript.
 These popups are styled by the browser and offer limited customisation.

                       JavaScript confirmations:
                       A confirm box is similar to an alert,
                       except the user can also choose to cancel the message.

See a sample confirm
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Firefox

# Click the link to activate the alert
driver.find_element(By.LINK_TEXT, "See a sample confirm").click()

# Wait for the alert to be displayed
wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.alert_is_present())

# Store the alert in a variable for reuse
alert = driver.switch_to.alert

# Store the alert text in a variable
text = alert.text

# Press the Cancel button
alert.dismiss()
