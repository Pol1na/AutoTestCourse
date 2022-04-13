import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('../chromedriver')
time.sleep(5)
try:
    browser.get(' http://suninjuly.github.io/find_xpath_form')
    input1 = browser.find_element(by=By.TAG_NAME, value="input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(by=By.NAME, value="last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(by=By.CLASS_NAME, value="city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(by=By.ID, value='country')
    input4.send_keys("Russia")
    # по Id
    #button = browser.find_element(by=By.ID, value='submit')
    button = browser.find_element(by=By.XPATH, value='//button[text()="Submit"]')
    button.click()
finally:
    time.sleep(30)
    browser.quit()

