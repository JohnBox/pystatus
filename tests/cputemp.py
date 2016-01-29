from components import cputemp
from tools import config

import subprocess as sp
import unittest


class TestCpuTemp(unittest.TestCase):
    def setUp(self):
        self.cfg = config.config('/home/gott/PycharmProjects/pystatus/pystatus.ini')
        self.cputemp = cputemp.CpuTemp(self.cfg['CPUTEMP'])

    def test_sensors(self):
        self.assertEqual(sp.check_call('sensors', stdout=sp.DEVNULL), 0, 'Not installed lm_sensors')

    def test_acpi(self):
        self.assertEqual(sp.check_call('acpi', stdout=sp.DEVNULL), 0, 'Not installed acpi')

if __name__ == '__main__':
    unittest.main()
