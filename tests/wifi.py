from pystatus import config
from components import wifi

import unittest


class TestWifi(unittest.TestCase):
    def setUp(self):
        self.cfg = config.config('/home/gott/PycharmProjects/pystatus/pystatus.ini')
        self.wifi = wifi.Wifi(self.cfg['WIFI'])

    def test_config(self):
        self.assertEqual(self.cfg['WIFI']['format'], '%(ssid) %(i[)')

    def test_wifi(self):
        pass

if __name__ == '__main__':
    unittest.main()
