# coding:utf-8
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
            1: "40,77",
            2: "112,77",
            3: "184,77",
            4: "256,77",
            5: "40,149",
            6: "112,149",
            7: "184,149",
            8: "256,149"
        }

    @classmethod
    def get_captcha_answer(cls, image_numbers):
        image_coordinate = cls.get_image_coordinate()
        answers = list(map(lambda num : image_coordinate.get(num), image_numbers))
        return ",".join(answers)
