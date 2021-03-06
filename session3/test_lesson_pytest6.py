from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import time
import math


@pytest.fixture
def browser():
    print('open browser')
    browser = webdriver.Chrome()
    yield browser
    print('\n close browser')
    browser.quit()


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                  'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1',
                                  'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1',
                                  'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1',
                                  'https://stepik.org/lesson/236905/step/1'])
class TestMethod:
    mylist = []

    def test_check_text_result(self, browser, link):
        browser.get(link)
        browser.implicitly_wait(3)
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, 'textarea'))
        ).send_keys(math.log(int(time.time())))
        browser.find_element(by=By.CSS_SELECTOR, value='.submit-submission').click()
        answer = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint'))
        ).text
        try:
            assert 'Correct!' == answer
        except AssertionError:
            self.mylist.append(answer)
