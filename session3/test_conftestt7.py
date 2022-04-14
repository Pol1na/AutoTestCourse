import pytest
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

link = "http://selenium1py.pythonanywhere.com/"


class TestMethod:
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(by=By.ID, value="login_link")
