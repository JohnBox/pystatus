from tools import config

import unittest


class TestBase(unittest.TestCase):
    def setUp(self):
        self.cfg = config.config('/home/gott/PycharmProjects/pystatus/pystatus.ini')

