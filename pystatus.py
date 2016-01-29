#!/usr/bin/env python
from tools import time, wifi, sound, cputemp, vk, battery, ram
import config
from json import dumps
from time import sleep
from sys import stdout


def main():
    cfg = config.config('/home/gott/PycharmProjects/pystatus/pystatus.ini')
    VERSION = {'version': 1}
    print(dumps(VERSION))
    print('[')
    interval = int(cfg['PYSTATUS']['refresh'])
    while True:
        t = time.Time(cfg['TIME'])
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
        print([t], end=',\n')
        sleep(interval)
        stdout.flush()

if __name__ == '__main__':
    main()

