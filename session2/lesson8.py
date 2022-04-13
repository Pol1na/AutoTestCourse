import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome('../chromedriver.exe')
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")
price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
browser.find_element(by=By.TAG_NAME, value='button').click()
browser.find_element(by=By.ID, value='price')
WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, 'input_value')))
x = browser.find_element(by=By.ID, value='input_value').text
answer = str(math.log(abs(12 * math.sin(int(x)))))
browser.find_element(by=By.TAG_NAME, value='input').send_keys(answer)
browser.find_element(by=By.ID, value='solve').click()

