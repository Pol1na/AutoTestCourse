from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome('../chromedriver.exe')
# добавляем к этому пути имя файла
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    browser.find_element(by=By.NAME, value="firstname").send_keys("check")
    browser.find_element(by=By.NAME, value="lastname").send_keys("check")
    browser.find_element(by=By.NAME, value="email").send_keys("check")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')
    print(file_path)
    input_ = browser.find_element(by=By.ID, value='file').send_keys(file_path)
    button = browser.find_element(by=By.CLASS_NAME, value="btn")
    button.click()
    time.sleep(5)
    welcome_text = browser.find_element(by=By.TAG_NAME, value="h1").text

finally:
    time.sleep(5)
    browser.quit()
