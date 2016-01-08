from tools import base
from json import dumps
from time import sleep

VERSION = {'version': 1}
b = base.Base('#444444')
print(dumps(VERSION))
print('[')
while True:
    print([b], end=',\n')
    sleep(3)
