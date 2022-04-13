import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('../chromedriver.exe')

try:
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(by=By.TAG_NAME, value='input')
    for element in elements:
        element.send_keys("изи")

    button = browser.find_element(by=By.CSS_SELECTOR, value="button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла