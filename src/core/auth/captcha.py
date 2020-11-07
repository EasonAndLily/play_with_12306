from PIL import Image
from src.core.tools import verify_code
from src.core.tools.utils import Utils
from src.core.tools.api_request import api


class Captcha(object):
    def __init__(self):
        self.__get_captcha_url = "https://kyfw.12306.cn/passport/captcha/captcha-image64"
        self.__check_captcha_url = "https://kyfw.12306.cn/passport/captcha/captcha-check"

    def get_captcha(self):
        res = api.get(self.__get_captcha_url)
        result = res.json()
        if "生成验证码成功" != result['result_message']:
            raise Exception("获取验证码失败，请确保您的计算机可以联网！")
        return result["image"]

    def check_captcha(self, answer):
        params = {
            "answer": answer,
            "rand": "sjrand",
            "login_site": "E"
        }
        res = api.post(self.__check_captcha_url, data=params)
        return res.json()["result_code"] == "4"

    def run(self, config):
        image_data = self.get_captcha()
        if config.CAPTCHA_IDENTIFY == 0:
            image_indexes = Captcha.verify_captcha_auto(image_data)
        elif config.CAPTCHA_IDENTIFY == 1:
            image_indexes = self.verify_captcha_manual(image_data)
        else:
            raise Exception("请配置图片验证码的验证方式！")

        print("输入的图片验证码序号为：" + ",".join(str(x) for x in image_indexes))
        answer = Utils.get_captcha_answer(image_indexes)
        check_result = self.check_captcha(answer)
        if check_result:
            print("验证码认证成功！")
            return answer
        else:
            raise Exception("验证码认证失败！")

    @classmethod
    def verify_captcha_auto(cls, image):
        answers = verify_code.verify(image)
        return list(map(int, answers))

    @classmethod
    def verify_captcha_manual(cls, image):
        Utils.save_captcha(image, Utils.get_captcha_path(), Utils.get_captcha_name())
        img = Image.open(Utils.get_captcha_path() + Utils.get_captcha_name())
        img.show()
        input_data = input("请输入符合的验证码图片序号(序号之间用英文逗号隔开，例如：3,8):")
        img.close()
        return list(map(int, input_data.split(",")))


if __name__ == '__main__':
    try:
        from config import config
        captcha = Captcha()
        captcha.run(config)
    except Exception as ex:
        print(ex)
        exit(0)
