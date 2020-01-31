# -*- coding: UTF-8 -*-
import datetime
import sys
from unittest import TestCase

import requests

sys.path.append('../../../src')
from core.ticket.ticket import Ticket


class TestTicket(TestCase):
    def setUp(self):
        self.ticket = Ticket()

    def test_query_left_tickets(self):
        left_tickets = self.ticket.query_left_tickets()
        self.assertEqual(len(left_tickets), 45)

    def test_parse_string_array_to_tickets(self):
        data = [
            "Avt7v3%2FScXNjDcCy48wu39Ovy0%2FV9jT%2BSsP312y5MW1v0b39rKwd20pv4Rhd%2FPcAGIp81XFCJbwD%0AwcrCT2%2FTw9gFa76trVzOmWAW6Z9mhMBDKm2B26bWgAEgN5PvWqjGbyxNQ4VbH0MD%2Bk6EcpnxU6gz%0ADFc8w7UhnoXGXKnFyrk4rN%2BAtBEvkaJyvJi8edl1KeEbOJKPzX%2FFX55b7FPU0NlSsFuz39SUB%2FVE%0Al0ToOwrnvwreP8i7OCo8CbVYS%2BDJpsmNnub%2BJKmDIwqZG5G5eRtEmxDz7Olsyq9BLOVtvT4BAgCg%0AYYsOHQ%3D%3D|预订|240000G1010P|G101|VNP|AOH|VNP|AOH|06:36|12:40|06:04|Y|V0w4kMkji7dLdZJ3PpJPP4ZuwPc8hX8JSBqkkaU7gc5gVtSV|20200227|3|P2|01|11|1|0|||||||||||有|有|无||O0M090|OM9|1|1|||||||||",
            "ctqm4oEOq0KUGhs4Yx6pY8dTdi94r26%2F28auSMC4%2B0fbL51DqsepgV7d2wazsodwoYyPAlJ2SBaf%0AiyppweRXhBh5C8cGsPLIpLAD8j6NqMtT8WaS8bDQNSMBJjvLY3V454ZH4eXYzmGJQt6SMLl4iHPZ%0AMRUoqR7ew0zpFxFBtiH6p75qYVICTH16gn%2BM53Qud78nK4oHFPB8FR4VCpHby6eM%2FNxgwfQU8bou%0A9FwUrykhoVSTfSR53FzKUs7yL22PfSBBChMU3OgTBSZ3Ohh5EnkycBsm4ckuFBjrsJg3c0Y%3D|预订|24000000G505|G5|VNP|SHH|VNP|SHH|07:00|11:40|04:40|Y|FiX%2BJJojKXsUM9hbSpJ6G5qmhYv8nGF4J9TP393aM0Nmg%2Bl3|20200227|3|P2|01|05|1|0|||||||||||有|有|无||O0M090|OM9|0|1|||||||||",
            "O%2FAKt9D4mfJUVgBxlUvttHF0wKxWl1dPfKkePvOZ4CfbWyh7%2F0MmH%2BdXdT2yjqZ3kHvP4figUezQ%0AWj%2BfJyfdhAZZ0dqBp3sl9ueV7TBqJ7a0rDibAFTrvUudmFFpIFqUR9Jbqb4hBqVlbpTtk%2FdCsqaW%0A5Yxv7fOM4pgLrxACEiDMifkA3mnMs%2F0972iInxYK61rr%2FxuxCS7Ccuku9Iqz3kTeAijkGD9j2gej%0AjesJNdmIIMZCb%2By8BI118ZibH%2BKHNVBPLGjoPh8lFBPXppalrWG2TuzPA5xPbmea8aqJzO8TfKCq%0AjjOv9Q%3D%3D|预订|240000G1050O|G105|VNP|AOH|VNP|AOH|07:20|13:08|05:48|Y|wzsbTJ7kU37QD4uxlhVYjo3afKgJL5jDLnipjCGTsP6SDt%2Fs|20200227|3|P4|01|10|1|0|||||||||||有|有|1||O0M090|OM9|1|0|||||||||",
            "JbangSOAujKjjjOeccaWrCsukPMPxPJe7eW4H3fk2EKGPBW7s8lqR2zJeJC8%2F1OUzfdPOwON5%2Ber%0AB6eiRlNzXSQC5ITXBJDzH5fNaVVLPdBssw5X0DIIJaSQCuDm0mU%2FvQLaeICZh8jHC3DtkDkD5uum%0AD83y7IuACfXe23GrLM0Bj5T9jmp2zXRvBXUOP7a3bWx3drZVCc%2BRKIxWaouz6euNQH1GdSVDz3C9%0AhHZJY7VNVFbH8wHWZ7k%2F8iFWXQD%2BkpDTynf86k8VN1kQKGXAq2CY%2BtL0F5Asg7eEgDj69NPhA0jg%0ASE4g7w%3D%3D|预订|240000G1130W|G113|VNP|AOH|VNP|AOH|08:50|14:33|05:43|Y|xnHD9n2dMXtMtNaXsSi3iskRv6dAxNOHp2igsZnSvbIL947%2B|20200227|3|P3|01|08|1|0|||||||||||有|有|无||O0M090|OM9|1|1|||||||||",
            "mMXaRkQgOlfIOfXEM1SRljbbMHHH5z0MT4R%2BVN4LKghGhjzxMfRDnGCWzQ7shIsp4ix5gzItJ5b0%0A1AvPQvUI%2FhWzBZW8YdSElqfwyFZEWiOLkaGTJlsy0PYevV9DXP93QuS6H7tPbthl75QfP9mOrDIu%0AyxHwg1DtxfBxJTTGko%2BKjNNRmsLlWtu%2FHfahsuO8WJIy8G7nmS0xzlj1cJ%2BLzev9USXorrpWgj2M%0A4flGy4R5wjc9Sk%2BCwF%2B345E%2FEAK7z6d0uDjk0bJzZCyNistZByF%2F1%2BDta6iDgwUv866tOZDpPvER%0A|预订|24000000G10G|G1|VNP|AOH|VNP|AOH|09:00|13:28|04:28|Y|iPV3KDZ30fsz5lzhxKKT4JwgSmG%2Bv53N2oe2VZsHoguTEX1R|20200227|3|P2|01|04|1|0|||||||||||有|有|无||O0M090|OM9|0|1|||||||||",
            "hNpI4O6KUE7EjNansiyl4rCRkRJpGenaDNwUu4nOmhz%2Fka8D8lbthleZfBRGp0n0aCCeYJyi4UUk%0AlxBahSwJgbk%2FIttuBxihqm4t%2BkBjBkOIqiLfzUVZys01DuGekLA7vFBAmzLsnlRRM%2BErUSpZlqpC%0AyW7kJy2e2XE2ijc0uyd8M5w1thVXCPAZ9%2FiqtcvgqnaJTPEf%2BxiPViCkhcgYW%2FZnHCZQQzjzIaBX%0AZ8lEQ4bB8hpcOPKj6G4zHGw88Zva%2BKOXHYprXVOdXom5YQnwXZmPdNXtHd2TDVks0neEsrOtWr72%0AvXvuqQ%3D%3D|预订|240000D70500|D705|BJP|SHH|BJP|SHH|21:21|09:21|12:00|Y|XONMe8QwCPJtkHOvWQEjEKPPSXF%2FYHbZ%2FtIZp0I8veidaQgfA3rOmCNUCMQ%3D|20200227|3|P4|01|04|0|0||||有|||有||有||有||||O0J0O0I0|OJOI|1|0|||||||||"]
        station_map = {"SHH": "上海", "VNP": "北京南", "BJP": "北京", "AOH": "上海虹桥", "SNH": "上海南"}
        left_tickets = Ticket.parse_string_array_to_tickets(data, station_map)
        self.assertEqual(len(left_tickets), 6)
        self.assertEqual(left_tickets[0]["trains_number"], "G101")
        self.assertIsNotNone(left_tickets[0]["train_secret"])
        self.assertEqual(left_tickets[0]["from_station"], "北京南")
        self.assertEqual(left_tickets[0]["end_station"], "上海虹桥")
        self.assertEqual(left_tickets[0]["start_time"], "06:36")
        self.assertEqual(left_tickets[0]["arrive_time"], "12:40")
        self.assertEqual(left_tickets[0]["duration"], "06:04")
        self.assertEqual(left_tickets[0]["business_class"], "无")
        self.assertEqual(left_tickets[0]["first_class"], "有")
        self.assertEqual(left_tickets[0]["second_class"], "有")
        self.assertEqual(left_tickets[0]["advance_soft_sleeper"], "")
        self.assertEqual(left_tickets[0]["bullet_train_sleeper"], "")
        self.assertIsNotNone(left_tickets[0]["soft_sleeper"])
        self.assertIsNotNone(left_tickets[0]["hard_sleeper"])
        self.assertEqual(left_tickets[0]["soft_seat"], "")
        self.assertIsNotNone(left_tickets[0]["hard_seat"])
        self.assertIsNotNone(left_tickets[0]["none_seat"])

    def test_can_book_specified_ticket(self):
        result = self.ticket.can_book_specified_ticket("G101", "hard_sleeper")
        self.assertFalse(result)
