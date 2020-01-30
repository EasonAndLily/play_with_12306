import json
import time


class GenerateHeaders(object):
    @classmethod
    def get_headers(cls):
        return {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/69.0.3497.100 Safari/537.36',
            "Host": "kyfw.12306.cn",
            "Origin": "https://kyfw.12306.cn",
            "Referer": "https://kyfw.12306.cn/otn/resources/login.html",
        }

    @classmethod
    def get_rail_expiration_device_id(cls):
        # timestamp = int(round(time.time() * 1000))
        # url = "https://kyfw.12306.cn/otn/HttpZF/logdevice?algID=4BbLmSosEH&hashCode=xm6v23GpXJkE8eByZcqL9cWy3Lqqz8s9NUbRG8hKnXE&FMQw=1&q4f3=en&VySQ=FGGaYCkR6vF4hcIljn2z5RvD7ZoZN5Vj&VPIf=1&custID=133&VEek=unknown&dzuS=0&yD16=0&EOQP=c227b88b01f5c513710d4b9f16a5ce52&jp76=52d67b2a5aa5e031084733d5006cc664&hAqN=MacIntel&platform=WEB&ks0Q=d22ca0b81584fbea62237b14bd04c866&TeRS=900x1440&tOHY=24xx900x1440&Fvje=i1l1o1s1&q5aJ=-8&wNLf=99115dfb07133750ba677d055874de87&0aew=Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010_13_3)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/79.0.3945.88%20Safari/537.36&E3gR=57e9a4845965065fe3e7f8f81bfb501e&timestamp=" + str(
        #     timestamp)
        # import requests
        # res = requests.get(url)
        # origin_data = res.text
        # start = origin_data.find('{')
        # end = origin_data.find('}')
        # data = json.loads(origin_data[start: end + 1])
        # return {
        #     "RAIL_EXPIRATION": data["exp"],
        #     "RAIL_DEVICEID": data["dfp"]
        # }
        return {
            "RAIL_EXPIRATION": "1580581700207",
            "RAIL_DEVICEID": "VTag2zFVgHmrCUf0WLCcq-tqRZh2ceEusCTZKxsgKIYyPg3JN0uFXOkgbRuYRYOLDSNfjRFGg6aoea_redAx2jKktgpsS6buUlmGp9l7jKt_qiZoRI4pKrPzaBc77Y2TT_TysPzeOuaLtwSkGgVyJAIk6Ri0ZwKv"
        }
