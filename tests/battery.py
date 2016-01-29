from components import battery
from tests import base

import unittest


class TestBattery(base.TestBase):
    def setUp(self):
        super().setUp()
        self.battery = battery.Battery(self.cfg['BATTERY'])

    def test_ac_on(self):
        self.assertEqual(self.battery.ac, 'on')
        self.assertEqual(self.battery.status, 'Unknown')
        self.assertEqual(self.battery.time, '')

    @unittest.expectedFailure
    def test_ac_off(self):
        self.assertEqual(self.battery.ac, 'off')
        self.assertEqual(self.battery.status, 'Discharging')

if __name__ == '__main__':
    unittest.main()
