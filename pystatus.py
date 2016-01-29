#!/usr/bin/env python
from tools import time, wifi, sound, cputemp, vk, battery, ram
from json import dumps
from time import sleep
from sys import stdout
from collections import OrderedDict

import config

def main():
    cfg = config.config('/home/gott/PycharmProjects/pystatus/pystatus.ini')
    VERSION = {'version': 1}
    print(dumps(VERSION))
    print('[')
    interval = int(cfg['PYSTATUS']['refresh'])
    panel = OrderedDict()
    panel['time'] = time.Time(cfg['TIME'])
    while True:
        # b = battery.Battery(config['BATTERY'])
        # w = wifi.Wifi(config['WIFI'])
        # s = sound.Sound(config['SOUND'])
        # c = cputemp.CpuTemp(config['CPUTEMP'])
        # r = ram.RAM(config['RAM'])
        # v = vk.VK(config['VK'])
        # if b.ac == 'off':
        #     panel = [v, r, c, s, w, b, t]
        # else:
        #     panel = [v, r, c, s, w, t]
        for item in panel:
            print([panel[item]], end=',\n')
        sleep(interval)
        stdout.flush()

if __name__ == '__main__':
    main()

