# Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
# Misc imports
from time import sleep

def screen(URL):
    # Setup webdriver

    DRIVER = 'resources/chromedriver'
    chromeOptions = Options()
    # chromeOptions.headless = True
    driver = webdriver.Chrome(DRIVER, options=chromeOptions)
    driver.set_window_size(('1920'),('1080'))
    driver.get(URL)

    # Get button for popup and click
    button = driver.find_element_by_class_name("close")
    button.click()
    html = driver.find_element_by_tag_name('html')

    # Page down and sleep
    html.send_keys(Keys.PAGE_DOWN)
    sleep(1)

    # Take Screen
    screenshot = driver.save_screenshot('images/image.png')
    driver.quit()