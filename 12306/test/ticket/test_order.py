# -*- coding: UTF-8 -*-
import sys
from unittest import TestCase

import requests

sys.path.append('../../../12306')
from core.ticket.order import Order


class TestOrder(TestCase):

    def test_submit_order(self):
        train_secret = "yOYid51PDEWBYXDxz71oqTYI3VDPiAkbqSJlFqn18XDWYauuk3mkkJ7CTQ6GJSCotvRb6xR1daH0" \
                       "zCPu/WQsk8mukd7GTD4ohny0Xr3L8tWDuTieWEjVUyHD+oQ5ETaEQYCX2X66lE0MrueppbDvSfwx" \
                       "tTnXh1cHLK5OYXomocU4CcrQvXr9X8lFcEFwgQA3CRqmNLNEhwtLiVK0C7oll+DeOgR66Oz0OwKN" \
                       "aV0KvP2kkD8sOtsrLhDg2NVhuY/64bWhd/7vgpnw27x47wKQPEBTIcTOXroM4QkT0f27sgo5Vmnu+tc+xQ=="
        order = Order("2020-02-19", u"北京", u"上海")
        session = requests.session()
        cookies_dict = {
            "JSESSIONID": "287C931E632E577D953A2755F4D499EB",
            "tk": "D-iHLex_MgueZIcivDXQv7bFNT6EWgGqi9qpEIpVu5krwl1l0",
            "_jc_save_wfdc_flag": "dc",
            "route": "6f50b51faa11b987e576cdb301e545c4",
            "RAIL_EXPIRATION": "1580298043097",
            "RAIL_DEVICEID": "EVIMU1jYDVkyksSaVXxTYsy7_cd83-PjlUrDny4ryTdeQya8HlhGEKHPibzbbRYh1mbZLQdgdmXERo2LvfyjGwbdZ6cqa347xM4JLSYC9HzFFtidLAHb5J3BhMUpeEFprEC9fHU14CAzNXm4U5f4cqTY5-cHJ96N",
            "_jc_save_fromDate": "2020-02-19",
            "_jc_save_toDate": "2020-02-19",
            "_jc_save_fromStation": "%u5317%u4EAC%2CBJP",
            "_jc_save_toStation": "%u4E0A%u6D77%2CSHH",
            "BIGipServerpassport": "971505930.50215.0000",
            "BIGipServerotn": "502268426.64545.0000",
            "BIGipServerpool_passport": "300745226.50215.0000"
        }
        session.cookies = requests.utils.cookiejar_from_dict(cookies_dict)
        result = order.submit_order(requests.session(), train_secret)
        self.assertTrue(result["status"])
        self.assertEqual("N", result["data"])
