import time

from selenium.webdriver import ActionChains

from src.core.auth.auth import Auth
from selenium import webdriver

from src.core.auth.captcha import Captcha
from src.core.tools.utils import Utils


class BrowserAuth(Auth):
    def __init__(self, config):
        super().__init__(config)
        self.login_url = "https://kyfw.12306.cn/otn/resources/login.html"
        self.driver = webdriver.Chrome()

    def login(self):
        self.open_login_form_page()
        self.fill_login_form()
        self.select_captcha_answers()
        self.submit_info()
        time.sleep(100)

    def open_login_form_page(self):
        self.driver.get(self.login_url)
        login_form = self.driver.find_element_by_css_selector('.login-hd-account').find_element_by_tag_name('a')
        actions = ActionChains(self.driver)
        actions.move_to_element(login_form)
        actions.click(login_form)
        actions.perform()

    def fill_login_form(self):
        username = self.driver.find_element_by_id("J-userName")
        username.send_keys(self.username)
        password = self.driver.find_element_by_id("J-password")
        password.send_keys(self.password)

    def select_captcha_answers(self):
        captcha = self.driver.find_element_by_id("J-loginImg")
        src = captcha.get_attribute('src')
        base64_image = src[22:]
        image_indexes = Captcha.verify_captcha_auto(base64_image)
        answers = Utils.get_captcha_answer_points(image_indexes)
        print(answers)
        click_area = self.driver.find_element_by_id("J-loginImgArea")
        actions = ActionChains(self.driver)
        for point in answers:
            actions.move_to_element(click_area)
            x_offset = point[0] - 150
            y_offset = point[1] - 96
            actions.move_by_offset(x_offset, y_offset).click()
        actions.perform()

    def submit_info(self):
        submit_btn = self.driver.find_element_by_id("J-login")
        actions = ActionChains(self.driver)
        actions.move_to_element(submit_btn).click().perform()
