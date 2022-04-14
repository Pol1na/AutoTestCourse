import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC

browser = webdriver.Chrome('../chromedriver.exe')
browser.get('https://www.demo.guru99.com/V4/')
browser.implicitly_wait(5)
browser.find_element(by=By.NAME, value='uid').send_keys('mngr399216')
browser.find_element(by=By.NAME, value='password').send_keys('azAzubU')
browser.find_element(by=By.NAME, value='btnLogin').click()
time.sleep(5)
browser.quit()