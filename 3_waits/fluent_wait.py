"""
https://www.selenium.dev/documentation/en/webdriver/waits/

 FluentWait

FluentWait instance defines the maximum amount of time to wait
for a condition, as well as the frequency with which to check the condition.

Users may configure the wait to ignore specific types of exceptions whilst waiting,
such as NoSuchElementException when searching for an element on the page.
"""
from telnetlib import EC

from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox
driver.get("http://somedomain/url_that_delays_loading")
wait = WebDriverWait(driver, 10, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div")))
