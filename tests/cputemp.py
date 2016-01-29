from components import cputemp
from tests import base
from tools import config

import subprocess as sp
import unittest


class TestCpuTemp(base.TestBase):
    def setUp(self):
        super().setUp()
        self.cputemp = cputemp.CpuTemp(self.cfg['CPUTEMP'])

    def test_sensors(self):
        self.assertEqual(sp.check_call('sensors', stdout=sp.DEVNULL), 0, 'Not installed lm_sensors')

    def test_acpi(self):
        self.assertEqual(sp.check_call('acpi', stdout=sp.DEVNULL), 0, 'Not installed acpi')

if __name__ == '__main__':
    unittest.main()
