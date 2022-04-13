import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome('../chromedriver.exe')
try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element(by=By.ID, value='input_value').text
    answer = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element(by=By.TAG_NAME, value='input').send_keys(answer)
    browser.execute_script("window.scrollBy(0, 150);")
    browser.find_element(by=By.ID, value='robotCheckbox').click()
    browser.find_element(by=By.ID, value='robotsRule').click()
    browser.find_element(by=By.ID, value='robotsRule').click()
    button = browser.find_element(by=By.TAG_NAME, value='button')
    button.click()

finally:
    time.sleep(5)
    browser.quit()

