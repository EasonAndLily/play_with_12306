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
        self.driver = BrowserAuth.generate_driver()

    def login(self):
        self.driver.get(self.login_url)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.open_login_form_page()
        self.fill_login_form()
        self.select_captcha_answers()
        self.submit_info()
        time.sleep(1)
        self.slider_verify()
        time.sleep(2)

    def save_cookies(self):
        cookies = self.driver.get_cookies()
        root_path = Utils.get_root_path()
        path = root_path + "/config"
        Utils.save_json_data_to_file(cookies, path, "cookies.json")
        self.driver.close()
        self.driver.quit()

    @staticmethod
    def generate_driver():
        options = webdriver.ChromeOptions()
        options.add_argument(
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/87.0.4280.67 Safari/537.36')
        options.add_argument("--no-sandbox")
        # options.add_argument("--headless") // if need run without window, use it
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        return driver

    def open_login_form_page(self):
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

    def slider_verify(self):
        slider = self.driver.find_element_by_id("nc_1_n1z")
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(slider, 300, 0).perform()
