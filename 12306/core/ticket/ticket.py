import requests


class Ticket(object):
    def __init__(self, from_station, end_station, train_date):
        self.__from_station = from_station
        self.__end_station = end_station
        self.__train_date = train_date
        self.__headers = {
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

    def query_left_tickets(self):
        basic_url = "https://kyfw.12306.cn/otn/leftTicket/queryZ?"
        url = basic_url + "leftTicketDTO.train_date=" + self.__train_date + "&leftTicketDTO.from_station=" + self.__from_station + "&leftTicketDTO.to_station=" + self.__end_station + "&purpose_codes=ADULT"
        session = requests.session()
        session.cookies = requests.utils.add_dict_to_cookiejar(session.cookies, {
            "Cookie": "tk=MmngS7iLqTdAWwXSl-DBpxVO6DrrOyGg4tjoOU9jifA1pl1l0; "
                      "JSESSIONID=FD244CE9309EEE78801430055243CC66; "
                      "RAIL_DEVICEID=BjIRSVVumHArn35g_X9jrAbQkR9pBaN34uNTTTeD30yzKjPy1Lw66hcxHssEad6Hj3MBSDuywDt6"
                      "b0A31wvNwY5cYFzuEByjhSPreuHB36CgbIKVqYjSDP_kMer8MkXZrWtMJmJf-pbZDGylBUog-e3w2RNJB2es"})

        res = session.get(url, headers=self.__headers)
        print res.text
        res.encoding = "utf-8"
        data = res.json()
        if data["httpstatus"] == 200:
            tickets = []
            station_number_map = data["data"]["map"]
            for item in data["data"]["result"]:
                info = item.split("|")
                result = dict()
                result.update({"trains_number": info[3]})
                result.update({"from_station": station_number_map[info[6]]})
                result.update({"end_station": station_number_map[info[7]]})
                result.update({"start_time": info[8]})
                result.update({"arrive_time": info[9]})
                result.update({"duration": info[10]})
                result.update({"business_class": info[32] or info[25]})
                result.update({"first_class": info[31]})
                result.update({"second_class": info[30]})
                result.update({"advance_soft_sleeper": info[21]})
                result.update({"bullet_train_sleeper": info[27]})
                result.update({"soft_sleeper": info[23]})
                result.update({"hard_sleeper": info[28]})
                result.update({"soft_seat": info[24]})
                result.update({"hard_seat": info[29]})
                result.update({"none_seat": info[26]})
                tickets.append(result)
            return tickets
