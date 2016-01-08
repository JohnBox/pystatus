from tools import time, wifi, sound, cputemp, vk
from config import Config
from json import dumps
from time import sleep

VERSION = {'version': 1}
print(dumps(VERSION))
print('[')

config = Config('/home/gott/PycharmProjects/pystatus/pystatus.ini')
interval = int(config.section('PYSTATUS')['interval'])
while True:
    t = time.Time(config.section('TIME'))
    w = wifi.Wifi(config.section('WIFI'))
    s = sound.Sound(config.section('SOUND'))
    c = cputemp.CpuTemp(config.section('CPUTEMP'))
    v = vk.VK(config.section('VK'))
    print([v, c, s, w, t], end=',\n')
    sleep(interval)
