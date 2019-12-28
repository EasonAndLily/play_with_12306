import json
import os

import requests


class Captcha(object):
    session = requests.session()

    @classmethod
    def get_captcha(cls):
        res = cls.session.get("https://kyfw.12306.cn/passport/captcha/captcha-image64")
        origin_data = res.text
        start = origin_data.find('{')
        end = origin_data.find('}')
        data = json.loads(origin_data[start: end + 1])
        return data['image']

    @classmethod
    def save_captcha(cls, image, path, file_name):
        import base64
        image_data = base64.b64decode(image)
        with open(path + file_name, 'wb') as f:
            f.write(image_data)

    @classmethod
    def check_captcha(cls, image_indexes):
        params = {
            "answer": cls.get_captcha_answer(image_indexes),
            "rand": "sjrand",
            "login_site": "E"
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
                          '/69.0.3497.100 Safari/537.36'
        }

        print "The image answers are: " + params["answer"]
        res = cls.session.post("https://kyfw.12306.cn/passport/captcha/captcha-check", data=params, headers=headers,
                               verify=False)
        is_successful = json.loads(res.text)["result_code"] == "4"
        return {
            "is_successful": is_successful,
            "answer": params["answer"]
        }

    @classmethod
    def get_captcha_answer(cls, image_numbers):
        image_coordinate = {
            1: "35,35",
            2: "115,35",
            3: "195,35",
            4: "445,35",
            5: "35,115",
            6: "115,115",
            7: "195,115",
            8: "445,115"
        }
        image_coordinate_str = ""
        for num in image_numbers:
            image_coordinate_str += "," + image_coordinate.get(num)

        return image_coordinate_str[1:]

    @classmethod
    def run(cls):
        image_data = Captcha.get_captcha()
        file_path = os.path.dirname(os.path.abspath(__file__))
        print file_path
        Captcha.save_captcha(image_data, file_path + "/", "captcha.jpg")
        from PIL import Image

        img = Image.open(file_path + '/captcha.jpg')
        img.show()
        image_numbers = []
        input_data = input("Please enter the right image indexes:")
        if type(input_data) == int:
            image_numbers.append(input_data)
        else:
            for number in input_data:
                image_numbers.append(number)
        print "The image index is: " + ",".join(str(x) for x in image_numbers)

        result = Captcha.check_captcha(image_numbers)
        if result["is_successful"]:
            print "Captcha check successfully!"
        else:
            print "Captcha check failed!"


if __name__ == '__main__':
    Captcha.run()
