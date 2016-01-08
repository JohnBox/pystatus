from tools import time, wifi, sound, cputemp
from json import dumps
from time import sleep

VERSION = {'version': 1}

print(dumps(VERSION))
print('[')
while True:
    t = time.Time('#00AFF0', '%T')
    w = wifi.Wifi('#0077B5')
    s = sound.Sound('#3F729B')
    c = cputemp.CpuTemp('#21759B')
    print([c, s, w, t], end=',\n')
    sleep(1)
