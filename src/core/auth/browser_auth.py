import time

from selenium.webdriver import ActionChains

from src.core.auth.auth import Auth
from selenium import webdriver


class BrowserAuth(Auth):
    def __init__(self, config):
        super().__init__(config)
        self.login_url = "https://kyfw.12306.cn/otn/resources/login.html"
        self.driver = webdriver.Chrome()

    def login(self):
        self.open_login_form_page()

    def open_login_form_page(self):
        self.driver.get(self.login_url)
        login_form = self.driver.find_element_by_css_selector('.login-hd-account').find_element_by_tag_name('a')
        actions = ActionChains(self.driver)
        actions.move_to_element(login_form)
        actions.click(login_form)
        actions.perform()
        time.sleep(10)

