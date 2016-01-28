#!/usr/bin/env python
from tools import time, wifi, sound, cputemp, vk, battery, ram
from json import dumps
from time import sleep
from sys import exit, stderr, stdout
from argparse import ArgumentParser
from configparser import ConfigParser

parser = ArgumentParser(description='Generate status line output for i3bar')
parser.add_argument('-c', '--config', help='absolute path to the config file', default='./pystatus.ini')
args = parser.parse_args()

if args.config:
    config = ConfigParser()
    config.read(args.config)
else:
    parser.print_usage(file=stderr)
    exit(1)

VERSION = {'version': 1}
print(dumps(VERSION))
print('[')

interval = int(config['PYSTATUS']['refresh'])
while True:
    t = time.Time(config['TIME'])
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
