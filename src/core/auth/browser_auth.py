import time

from selenium.webdriver import ActionChains

from src.core.auth.auth import Auth
from selenium import webdriver


class BrowserAuth(Auth):
    def __init__(self, config):
        super().__init__(config)

    def login(self):
        self.open_login_form_page()

    def open_login_form_page(self):
        driver = self.get_web_driver()
        driver.get("https://kyfw.12306.cn/otn/resources/login.html")
        login_form = driver.find_element_by_css_selector('.login-hd-account').find_element_by_tag_name('a')
        actions = ActionChains(driver)
        actions.move_to_element(login_form)
        actions.click(login_form)
        actions.perform()
        time.sleep(10)


    @classmethod
    def get_web_driver(cls):
        options = webdriver.ChromeOptions()
        options.add_argument(
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36')
        options.add_argument("--no-sandbox")
        options.add_argument("--headless")
        return webdriver.Chrome()
