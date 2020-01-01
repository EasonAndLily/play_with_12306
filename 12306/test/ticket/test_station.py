# -*- coding: UTF-8 -*-
import sys
from unittest import TestCase

sys.path.append('../../../12306')
from core.ticket.station import Station


class TestStation(TestCase):
    station = Station()

    def test_get_stations_values_keys(self):
        stations = TestStation.station.get_stations_values_keys()
        self.assertIsNotNone(stations)
        self.assertEqual(stations["VAP"], u"北京北")

    def test_get_stations_keys_values(self):
        stations = TestStation.station.get_stations_keys_values()
        self.assertIsNotNone(stations)
        self.assertEqual(stations[u"北京北"], "VAP")
