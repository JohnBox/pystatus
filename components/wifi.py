from .base import Base
from subprocess import Popen, PIPE
import re
import math
from time import sleep


class Wifi(Base):
    QUALITIES = ['E', 'D', 'C', 'B', 'A']

    def __init__(self, cfg):
        super().__init__(cfg)

        self.downup_re = re.compile('\((\d.+?)\)', re.M)
        self.ip_re = re.compile('inet (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})')
        self.ssid_re = re.compile('"(.+?)"')
        self.quality_re = re.compile('(\d{1,2}/\d{2})')
        self.refresh()

    def refresh(self):
        try:
            ifconfig = Popen(['ifconfig', self.cfg['interface']], stdout=PIPE).stdout.read().decode().rstrip()
            self.down, self.up = self.downup_re.findall(ifconfig)
            self.down, self.up = self.down.replace('iB', '').replace(' ', ''), self.up.replace('iB', '').replace(' ', '')
            self.ip = self.ip_re.search(ifconfig).group(1)

            iwconfig = Popen(['iwconfig', self.cfg['interface']], stdout=PIPE).stdout.read().decode().rstrip()
            self.ssid = self.ssid_re.search(iwconfig).group(1)
            self.quality = self.quality_re.search(iwconfig).group(1)
            self.quality = math.floor(eval(self.quality)*len(Wifi.QUALITIES)-1)
            self.quality = Wifi.QUALITIES[self.quality]

            params = {
                'down': self.down,
                'up': self.up,
                'ip': self.ip,
                'ssid': self.ssid,
                'quality': self.quality
            }
            self.full_text = self.cfg['format'] % params
        except:
            pass
