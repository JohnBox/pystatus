from tools import time
from json import dumps
from time import sleep

VERSION = {'version': 1}
b = time.Time('#00AFF0')
print(dumps(VERSION))
print('[')
while True:
    print([b, b], end=',\n')
    sleep(3)
