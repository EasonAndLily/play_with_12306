import json

import requests


class Captcha(object):

    @classmethod
    def get_captcha(cls):
        res = requests.get("https://kyfw.12306.cn/passport/captcha/captcha-image64")
        origin_data = res.text
        start = origin_data.find('{')
        end = origin_data.find('}')
        data = json.loads(origin_data[start: end + 1])
        return {
            "image_id": res.cookies["_passport_ct"],
            "image": data['image']
        }

    @classmethod
    def save_captcha(cls, image, path, file_name):
        import base64
        image_data = base64.b64decode(image["image"])
        with open(path + file_name, 'wb') as f:
            f.write(image_data)

    @classmethod
    def check_captcha(cls, image_numbers, image_id):
        params = {
            "callback": "jQuery19101703802021034182_1577457464415",
            "answer": cls.get_captcha_answer(image_numbers),
            "rand": "sjrand",
            "login_site": "E"
        }
        res = requests.get("https://kyfw.12306.cn/passport/captcha/captcha-check", params=params,
                           cookies={'_passport_ct': image_id})
        origin_data = res.text
        start = origin_data.find('{')
        end = origin_data.find('}')
        data = json.loads(origin_data[start: end + 1])
        return data["result_code"] == "4"

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
        for number in image_numbers:
            image_coordinate_str += "," + image_coordinate.get(number)

        return image_coordinate_str[1:]
