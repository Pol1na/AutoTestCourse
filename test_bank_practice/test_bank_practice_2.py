import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

link = 'https://www.demo.guru99.com/V4/'


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    print('\nstart browser')
    browser.get(link)
    browser.implicitly_wait(3)
    return browser


class TestMethod1:
    def test_auth(self, browser):
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "uid"))
        ).send_keys('mngr399216')
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        ).send_keys('azAzubU')
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "btnLogin"))
        ).click()
        title = WebDriverWait(browser, 10).until((
            EC.presence_of_element_located((By.CLASS_NAME, 'barone'))
        )).text
        assert title == 'Guru99 Bank', 'Wrong title'
