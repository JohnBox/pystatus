from components import wifi
from tests import base
from tools import config

import unittest


class TestWifi(base.TestBase):
    def setUp(self):
        super().setUp()
        self.wifi = wifi.Wifi(self.cfg['WIFI'])

    def test_config(self):
        self.assertEqual(self.cfg['WIFI']['format'], '%(ssid)s %(quality)s %(down)s')

    def test_ip(self):
        import socket
        ip = socket.gethostbyname(socket.gethostname())
        self.assertEqual(self.wifi.ip, ip)

    @unittest.expectedFailure
    def test_quality(self):
        self.assertEqual(self.wifi.quality, 'A')

if __name__ == '__main__':
    unittest.main()
