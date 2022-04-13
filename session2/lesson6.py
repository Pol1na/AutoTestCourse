import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome('../chromedriver.exe')
    browser.get('http://suninjuly.github.io/alert_accept.html')
    browser.find_element(by=By.TAG_NAME, value="button").click()
    browser.switch_to.alert.accept()
    time.sleep(1)
    x = browser.find_element(by=By.ID, value="input_value").text
    answer = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element(by=By.TAG_NAME, value='input').send_keys(answer)
    browser.find_element(by=By.TAG_NAME, value='button').click()
    print(browser.switch_to.alert.text.split(':')[1])


finally:
    time.sleep(5)
    browser.quit()