from .base import Base
from subprocess import Popen, PIPE
import re
import math
from time import sleep


class Wifi(Base):
    QUALITIES = ['A', 'B', 'C', 'D', 'E'][::-1]

    def __init__(self, cfg):
        Base.__init__(self, cfg['color'])
        try:
            ifconfig = Popen(['ifconfig', cfg['interface']], stdout=PIPE).stdout.read().decode().rstrip()
            iwconfig = Popen(['iwconfig', cfg['interface']], stdout=PIPE).stdout.read().decode().rstrip()
            pattif = re.compile('inet (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).*?\((\d+).\d (\w+).*?\((\d+).\d (\w+)', re.I | re.M | re.S)
            pattiw = re.compile('ESSID:"(.*?)".*?Quality=(.*?)  Signal', re.I | re.M | re.S)
            ip, *downup = pattif.findall(ifconfig)[0]
            down = downup[0] + downup[1].replace('iB', '')
            up = downup[2] + downup[3].replace('iB', '')
            ssid, quality = pattiw.findall(iwconfig)[0]
            quality = math.floor(eval(quality)*5-1)
            quality = Wifi.QUALITIES[quality]
            self.full_text = '%s [%s] %s' % (ssid, quality, down)
        except:
            pass
