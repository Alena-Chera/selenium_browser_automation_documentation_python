from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By


def document_initialised(driver):
    return driver.execute_script("return initialised")


driver = webdriver.Firefox()
driver.get("file:///race_condition.html")
WebDriverWait(driver).until(document_initialised)
el = driver.find_element(By.TAG_NAME, "p")
assert el.text == "Hello from JavaScript!"

# because the wait utility ignores no such element errors by default, we can refactor our instructions to be more
# concise:

el = WebDriverWait(driver).until(lambda d: d.find_element_by_tag_name("p"))
assert el.text == "Hello from JavaScript!"


# The wait lets you pass in an argument to override the timeout:
# WebDriverWait(driver, timeout=3).until(some_condition)

#              Expected conditions

# The conditions available in the different language bindings vary, but this is a non-exhaustive list of a few:
#
# alert is present
# element exists
# element is visible
# title contains
# title is
# element staleness
# visible text
