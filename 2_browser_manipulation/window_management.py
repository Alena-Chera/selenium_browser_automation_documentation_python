"""
https://www.selenium.dev/documentation/en/webdriver/browser_manipulation/
"""

"""
Get window size:
(Fetches the size of the browser window in pixels)
"""
from selenium import webdriver

with webdriver.Firefox() as driver:
    # Access each dimension individually
    width = driver.get_window_size().get("width")
    height = driver.get_window_size().get("height")

    # Or store the dimensions and query them later
    size = driver.get_window_size()
    width1 = size.get("width")
    height1 = size.get("height")


"""
Set window size:
(Restores the window and sets the window size)
"""
driver.set_window_size(1024, 768)