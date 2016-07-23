#!/usr/bin/env python
from components import time, wifi, ethernet, sound, cputemp, cpufan, vk, battery, ram
from json import dumps
from time import sleep
from sys import stdout
from collections import OrderedDict

from tools import parser
import time as t

def main():
    cfg = parser.parse('./pystatus.ini')
    VERSION = {'version': 1}
    print(dumps(VERSION))
    # print('[')
    interval = float(cfg['PYSTATUS'].get('refresh', '1'))
    panel = OrderedDict()
    panel['time'] = time.Time(cfg['TIME'])
    panel['battery'] = battery.Battery(cfg['BATTERY'])
    panel['sound'] = sound.Sound(cfg['SOUND'])
    # panel['wifi'] = wifi.Wifi(cfg['WIFI'])
    # panel['ethernet'] = ethernet.Ethernet(cfg['ETHERNET'])
    panel['cputemp'] = cputemp.CpuTemp(cfg['CPUTEMP'])
    # panel['cpufan'] = cpufan.CpuFan(cfg['CPUFAN'])
    panel['ram'] = ram.RAM(cfg['RAM'])
    # panel['vk'] = vk.VK(cfg['VK'])
    # panel['gmail'] = gmail.Gmail(cfg['GMAIL'])
    while True:
        start = t.time()
        visibled = list(filter(lambda i: i.visible, reversed(list(panel.values()))))
        print(visibled, end=',\n')
        list(map(lambda i: i.refresh(), panel.values()))
        late = t.time() - start

        sleep((interval - late) if (interval - late) > 0 else interval)
        stdout.flush()

if __name__ == '__main__':
    main()

