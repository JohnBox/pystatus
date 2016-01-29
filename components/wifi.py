from .base import Base
from subprocess import Popen, PIPE
import re
import math
from time import sleep


class Wifi(Base):
    QUALITIES = ['E', 'D', 'C', 'B', 'A']

    def __init__(self, cfg):
        super().__init__(cfg)
        self.refresh()

    def refresh(self):
        try:
            ifconfig = Popen(['ifconfig', self.cfg['interface']], stdout=PIPE).stdout.read().decode().rstrip()
            downup_re = re.compile('\((\d.+?)\)', re.M)
            ipre = re.compile('inet (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})')
            down, up = downup_re.findall(ifconfig)
            down, up = down.replace('iB', '').replace(' ', ''), up.replace('iB', '').replace(' ', '')
            ip = ipre.search(ifconfig).group(1)
            iwconfig = Popen(['iwconfig', self.cfg['interface']], stdout=PIPE).stdout.read().decode().rstrip()
            ssidre = re.compile('"(.+?)"')
            ssid = ssidre.search(iwconfig).group(1)
            quality_re = re.compile('(\d{1,2}/\d{2})')
            quality = quality_re.search(iwconfig).group(1)
            quality = math.floor(eval(quality)*5-1)
            quality = Wifi.QUALITIES[quality]
            params = {
                'down': down,
                'up': up,
                'ip': ip,
                'ssid': ssid,
                'quality': quality
            }
            self.full_text = self.cfg['format'] % params
        except:
            pass
