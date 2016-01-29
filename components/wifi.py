from .base import Base
from subprocess import Popen, PIPE
import re
import math
from time import sleep


class Wifi(Base):
    QUALITIES = ['E', 'D', 'C', 'B', 'A']

    def __init__(self, cfg):
        Base.__init__(self, cfg['color'])
        try:
            ifconfig = Popen(['ifconfig', cfg['interface']], stdout=PIPE).stdout.read().decode().rstrip()
            downupre = re.compile('\((\d.+?)\)', re.M)
            ipre = re.compile('inet (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})')
            down, up = downupre.findall(ifconfig)
            down, up = down.replace('iB', '').replace(' ', ''), up.replace('iB', '').replace(' ', '')
            ip = ipre.search(ifconfig).group(1)
            iwconfig = Popen(['iwconfig', cfg['interface']], stdout=PIPE).stdout.read().decode().rstrip()
            ssidre = re.compile('"(.+?)"')
            ssid = ssidre.search(iwconfig).group(1)
            qualityre = re.compile('(\d{1,2}/\d{2})')
            quality = qualityre.search(iwconfig).group(1)
            quality = math.floor(eval(quality)*5-1)
            quality = Wifi.QUALITIES[quality]
            self.full_text = '%(ssid)s [%(quality)s] %(down)s' % locals()
        except:
            pass
