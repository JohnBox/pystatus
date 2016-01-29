from components import vk as _vk
from tests import base

import unittest


class TestBattery(base.TestBase):
    def setUp(self):
        super().setUp()
        self.__vk = _vk.VK(self.cfg['VK'])

    # TODO
    @unittest.expectedFailure
    def test_count(self):
        self.assertEqual(self.__vk.count, 0)

if __name__ == '__main__':
    unittest.main()

