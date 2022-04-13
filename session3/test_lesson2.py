import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


def open_browser(link):
    browser = webdriver.Chrome('../chromedriver.exe')
    browser.get(link)
    browser.find_element(by=By.CSS_SELECTOR, value=".first_block .first").send_keys("check")
    browser.find_element(by=By.CSS_SELECTOR, value=".first_block .second").send_keys("check")
    browser.find_element(by=By.CSS_SELECTOR, value=".first_block .third").send_keys("check")
    browser.find_element(by=By.CLASS_NAME, value="btn").click()
    return browser.find_element(by=By.TAG_NAME, value="h1").text


class TestRegistration(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(open_browser('http://suninjuly.github.io/registration1.html'),
                         'Congratulations! You have successfully registered!', 'registration is failed')

    def test_reg2(self):
        self.assertEqual(open_browser('http://suninjuly.github.io/registration2.html'),
                         'Congratulations! You have successfully registered!', 'registration is failed')


if __name__ == "__main__":
    unittest.main()

# class TestRegistration(unittest.TestCase):
#     def test_first_name(self):
#         browser = webdriver.Chrome('../chromedriver.exe')
#         link = "http://suninjuly.github.io/registration2.html"
#         browser.get(link)
#         browser.find_element(by=By.CSS_SELECTOR, value=".first_block .first").send_keys("check")
#         button = browser.find_element(by=By.CLASS_NAME, value="btn")
#         button.click()
#         browser.quit()
#
#     def test_second_name(self):
#         browser = webdriver.Chrome('../chromedriver.exe')
#         link = "http://suninjuly.github.io/registration2.html"
#         browser.get(link)
#         self.assertEqual(browser.find_element(by=By.CSS_SELECTOR, value=".first_block .second").send_keys("check"), None, 'wrong')
#         button = browser.find_element(by=By.CLASS_NAME, value="btn")
#         button.click()
#         browser.quit()
#
#     def test_patronymic(self):
#         browser = webdriver.Chrome('../chromedriver.exe')
#         link = "http://suninjuly.github.io/registration2.html"
#         browser.get(link)
#         browser.find_element(by=By.CSS_SELECTOR, value=".first_block .third").send_keys("check")
#         button = browser.find_element(by=By.CLASS_NAME, value="btn")
#         button.click()
#         browser.quit()


if __name__ == "__main__":
    unittest.main()
