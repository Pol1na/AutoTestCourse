import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome('../chromedriver.exe')
    browser.get('http://suninjuly.github.io/get_attribute.html')
    x = browser.find_element(by=By.ID, value='treasure').get_attribute('valuex')
    answer = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element(by=By.ID, value='answer').send_keys(answer)
    browser.find_element(by=By.ID, value='robotCheckbox').click()
    browser.find_element(by=By.ID, value='robotsRule').click()
    browser.find_element(by=By.CSS_SELECTOR, value='.btn').click()


finally:
    time.sleep(5)
    browser.quit()
