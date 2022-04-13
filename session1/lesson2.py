import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome('../chromedriver.exe')
time.sleep(2)
try:
    browser.get('http://suninjuly.github.io/find_link_text')
    text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link = browser.find_element(by=By.PARTIAL_LINK_TEXT, value=text)
    link.click()
    input1 = browser.find_element(by=By.TAG_NAME, value="input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(by=By.NAME, value="last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(by=By.CLASS_NAME, value="city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(by=By.ID, value='country')
    input4.send_keys("Russia")
    button = browser.find_element(by=By.CLASS_NAME, value='btn-default')
    button.click()
finally:
    time.sleep(30)
    browser.quit()