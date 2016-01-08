from tools import time, wifi
from json import dumps
from time import sleep

VERSION = {'version': 1}

print(dumps(VERSION))
print('[')
while True:
    t = time.Time('#00AFF0', '%T')
    w = wifi.Wifi('#0077B5')
    print([w, t], end=',\n')
    sleep(1)
