# coding:utf-8
import base64
import binascii
import datetime
import json
import os


class Utils(object):

    @classmethod
    def get_root_path(cls):
        project_name = "play_with_12306"
        current_path = os.path.abspath(os.path.dirname(__file__))
        return current_path[:current_path.find(project_name) + len(project_name)]

    @classmethod
    def get_captcha_path(cls):
        root_path = cls.get_root_path()
        return root_path + "/config/"

    @classmethod
    def get_captcha_name(cls):
        return "captcha.jpg"

    @classmethod
    def get_image_coordinate(cls):
        return {
            1: (30, 67),
            2: (102, 67),
            3: (174, 67),
            4: (246, 67),
            5: (30, 139),
            6: (102, 139),
            7: (174, 139),
            8: (246, 139)
        }

    @classmethod
    def get_captcha_answer(cls, image_numbers):
        image_coordinate = cls.get_image_coordinate()
        answers = list(map(lambda num: ",".join(map(str, image_coordinate.get(num))), image_numbers))
        return ",".join(answers)

    @classmethod
    def get_captcha_answer_points(cls, image_numbers):
        image_coordinate = cls.get_image_coordinate()
        return list(map(lambda num: image_coordinate.get(num), image_numbers))

    @classmethod
    def save_captcha(cls, image, path, file_name):
        import base64
        image_data = base64.b64decode(image)
        with open(path + file_name, 'wb') as f:
            f.write(image_data)

    @classmethod
    def save_json_data_to_file(cls, json_data, file_path, file_name):
        path = os.path.join(file_path, file_name)
        with open(path, 'w') as outfile:
            json.dump(json_data, outfile)

    @classmethod
    def get_json_data_from_file(cls, file_path, file_name):
        path = os.path.join(file_path, file_name)
        with open(path) as json_file:
            return json.load(json_file)

    @classmethod
    def validate_time_format(cls, time_str):
        try:
            datetime.datetime.strptime(time_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    @classmethod
    def current_date(cls):
        return datetime.datetime.now().strftime('%Y-%m-%d')

    @classmethod
    def is_today(cls, time_str):
        date_time = datetime.datetime.strptime(time_str, '%Y-%m-%d  %H:%M:%S')
        return date_time.date().strftime("%Y-%m-%d") == cls.current_date()

    @classmethod
    def check_time_in_correct_range(cls, time_str):
        today = datetime.datetime.strptime(cls.current_date(), '%Y-%m-%d')
        depart_day = datetime.datetime.strptime(time_str, '%Y-%m-%d')
        difference = (depart_day - today).days
        return 29 >= difference >= 0

    @classmethod
    def is_base64(cls, s):
        try:
            base64.decodebytes(s)
            return True
        except binascii.Error:
            return False
