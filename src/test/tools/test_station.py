# -*- coding: UTF-8 -*-
import sys
from unittest import TestCase

sys.path.append('../../../src')
from core.tools.station import Station


class TestStation(TestCase):

    def test_get_station_value_by_key(self):
        station = Station()
        value = station.get_stations_value_by_key("VAP")
        self.assertIsNotNone(value)
        self.assertEqual(value, "北京北")

    def test_get_station_key_by_values(self):
        station = Station()
        key = station.get_station_key_by_values("北京北")
        self.assertIsNotNone(key)
        self.assertEqual(key, "VAP")

    def test_request_stations(self):
        stations = Station.request_stations()
        self.assertIsNotNone(stations)

    def test_has_this_station(self):
        station = Station()
        exist = station.has_this_station("上海")
        self.assertTrue(exist)
        not_exist = station.has_this_station("不知道")
        self.assertFalse(not_exist)
