from components import ram
from tests import base
from tools import config

import subprocess as sp
import unittest


class TestRam(base.TestBase):
    def setUp(self):
        super().setUp()
        self.ram = ram.RAM(self.cfg['RAM'])

if __name__ == '__main__':
    unittest.main()