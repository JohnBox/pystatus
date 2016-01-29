#!/usr/bin/env python
from components import time, wifi, sound, cputemp, vk, battery, ram
from json import dumps
from time import sleep
from sys import stdout
from collections import OrderedDict

from tools import parser


def main():
    # cfg = parser.parse('/home/gott/PycharmProjects/pystatus/pystatus.ini')
    cfg = parser.parse('./pystatus.ini')
    VERSION = {'version': 1}
    print(dumps(VERSION))
    print('[')
    interval = int(cfg['PYSTATUS']['refresh'])
    panel = OrderedDict()
    panel['time'] = time.Time(cfg['TIME'])
    panel['wifi'] = wifi.Wifi(cfg['WIFI'])
    panel['cputemp'] = cputemp.CpuTemp(cfg['CPUTEMP'])
    # b = battery.Battery(config['BATTERY'])
    # s = sound.Sound(config['SOUND'])
    # r = ram.RAM(config['RAM'])
    # v = vk.VK(config['VK'])
    while True:
        visibled = list(filter(lambda i: i.visible, reversed(panel.values())))
        print(visibled, end=',\n')
        list(map(lambda i: i.refresh(), panel.values()))
        sleep(interval)
        stdout.flush()

if __name__ == '__main__':
    main()

