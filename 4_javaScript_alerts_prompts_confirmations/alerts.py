"""
https://www.selenium.dev/documentation/en/webdriver/js_alerts_prompts_and_confirmations/

 JavaScript alerts, prompts and confirmations
 WebDriver provides an API for working with the three types of native popup messages offered by JavaScript.
 These popups are styled by the browser and offer limited customisation.

                       JavaScript alerts:
                       The simplest of these is referred to as an alert, which shows a custom message,
                       and a single button which dismisses the alert, labelled in most browsers as OK.
                       It can also be dismissed in most browsers by pressing the close button,
                       but this will always do the same thing as the OK button.
                       WebDriver can get the text from the popup
                       and accept or dismiss these alerts.
 See an example alert
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Firefox
# Click the link to activate the alert
driver.find_element(By.LINK_TEXT, "See an example alert").click()

# Wait for the alert to be displayed and store it in a variable
wait = WebDriverWait(driver, 15)

alert = wait.until(expected_conditions.alert_is_present())

# Store the alert text in a variable
text = alert.text

# Press the OK button
alert.accept()
