from .base import Base
from subprocess import Popen, PIPE
import re
import math


class Wifi(Base):
    QUALITIES = ['A', 'B', 'C', 'D', 'E'][::-1]

    def __init__(self, color, iface='wlp2s0'):
        Base.__init__(self, color)
        ifconfig = Popen(['ifconfig', iface], stdout=PIPE).stdout.read().decode().rstrip()
        iwconfig = Popen(['iwconfig', iface], stdout=PIPE).stdout.read().decode().rstrip()
        pattif = re.compile('inet (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).*?\((\d+).\d (\w+).*?\((\d+).\d (\w+)', re.I | re.M | re.S)
        pattiw = re.compile('ESSID:"(.*?)".*?Quality=(.*?)  Signal', re.I | re.M | re.S)
        ip, *downup = pattif.findall(ifconfig)[0]
        down = downup[0] + downup[1].replace('i', '')
        up = downup[2] + downup[3].replace('i', '')
        ssid, quality = pattiw.findall(iwconfig)[0]
        quality = math.floor(eval(quality)*5-1)
        quality = Wifi.QUALITIES[quality]

        self.full_text = '%s[%s] %s' % (ssid, quality, down)
