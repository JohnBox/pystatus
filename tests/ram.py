from components import ram
from tests import base

import subprocess as sp
import unittest


class TestRam(base.TestBase):
    def setUp(self):
        super().setUp()
        self.ram = ram.RAM(self.cfg['RAM'])

    def test_free_ram(self):
        import re
        free = sp.Popen(['free', '-h', '--si'], stdout=sp.PIPE).stdout
        free = sp.Popen(['head', '-2'], stdin=free, stdout=sp.PIPE).stdout
        free = sp.Popen(['tail', '-1'], stdin=free, stdout=sp.PIPE).stdout.read().decode().strip()
        self.assertEqual(self.ram.free, re.split('\s+', free)[3].replace(',', '.'))

if __name__ == '__main__':
    unittest.main()
