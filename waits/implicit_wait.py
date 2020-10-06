"""
https://www.selenium.dev/documentation/en/webdriver/waits/

 Implicit wait
"""

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox

driver.implicitly_wait(10)

driver.get("http://somedomain/url_that_delays_loading")
my_dynamic_element = driver.find_element(By.ID, "myDynamicElement")
