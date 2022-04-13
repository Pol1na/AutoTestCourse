from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome("../chromedriver.exe")
    browser.get(link)
    browser.find_element(by=By.CSS_SELECTOR, value=".first_block .first").send_keys("check")
    browser.find_element(by=By.CSS_SELECTOR, value=".first_block .second").send_keys("check")
    browser.find_element(by=By.CSS_SELECTOR, value=".first_block .third").send_keys("check")
    button = browser.find_element(by=By.CLASS_NAME, value="btn")
    button.click()
    time.sleep(5)
    welcome_text = browser.find_element(by=By.TAG_NAME, value="h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    browser.quit()
