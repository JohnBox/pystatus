from tools import time
from pystatus import config

import unittest


class TestTime(unittest.TestCase):
    def setUp(self):
        self.cfg = config.config('/home/gott/PycharmProjects/pystatus/pystatus.ini')
        self.time = time.Time(self.cfg['TIME'])

    def test_config(self):
        self.assertEqual(self.cfg['TIME']['format'], '%a %d/%m %R')

    def test_time(self):
        from datetime import datetime
        self.assertEqual(datetime.now().time().s, self.time.full_text)

if __name__ == '__main__':
    unittest.main()
