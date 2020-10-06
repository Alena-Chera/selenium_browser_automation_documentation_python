"""
https://www.selenium.dev/documentation/en/webdriver/browser_manipulation/
Window management
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

"""
Get window position:
"""
# Access each dimension individually
x = driver.get_window_position().get('x')
y = driver.get_window_position().get('y')

# Or store the dimensions and query them later
position = driver.get_window_position()
x1 = position.get('x')
y1 = position.get('y')

"""
Set window position:
"""
# Move the window to the top left of the primary monitor
driver.set_window_position(0, 0)

"""
Maximise window:
"""
driver.maximize_window()

"""
Minimize window:
"""
driver.minimize_window()

"""
Fullscreen window:
"""
driver.fullscreen_window()

"""
Take Screenshot:
"""
from selenium import webdriver

driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.example.com")

# Returns and base64 encoded string into image
driver.save_screenshot('./image.png')

driver.quit()

"""
TakeElementScreenshot:
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.example.com")

ele = driver.find_element(By.CSS_SELECTOR, 'h1')

# Returns and base64 encoded string into image
ele.screenshot('./image.png')

driver.quit()
