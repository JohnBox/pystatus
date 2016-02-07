from .base import Base
from subprocess import Popen, PIPE
from sys import stderr

import math
import re
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
            ifconfig = Popen(['ifconfig', self.cfg.get('interface', 'wlp2s0')], stdout=PIPE).stdout.read().decode().rstrip()
            self.ip = self.ip_re.search(ifconfig)
            if self.ip:
                self.ip = self.ip.group(1)
                self.down, self.up = self.downup_re.findall(ifconfig)
                self.down, self.up = self.down.replace('iB', '').replace(' ', ''), self.up.replace('iB', '').replace(' ', '')

                iwconfig = Popen(['iwconfig', self.cfg.get('interface', 'wlp2s0')], stdout=PIPE).stdout.read().decode().rstrip()
                self.ssid = self.ssid_re.search(iwconfig).group(1)
                self.quality = self.quality_re.search(iwconfig).group(1)
                # quality is str like 'x/y'
                self.quality = '0.5'
                self.quality = eval(self.quality) - 0.5
                self.quality = math.ceil(round(self.quality * 10, 2)) - 1
                if self.quality < 0:
                    self.quality = abs(self.quality) - 1
                    self.quality = Wifi.QUALITIES[self.quality]
                    self.quality = '-' + self.quality
                else:
                    self.quality = Wifi.QUALITIES[self.quality]

                params = {
                    'down': self.down,
                    'up': self.up,
                    'ip': self.ip,
                    'ssid': self.ssid,
                    'quality': self.quality
                }
                self.full_text = self.cfg.get('format', '%(ssid)s %(quality)s %(ip)s') % params
            else:
                self.full_text = ''
        except Exception as e:
            print(e, file=stderr)
            pass
