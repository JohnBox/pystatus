from .base import Base as __Base
from subprocess import Popen, PIPE
from sys import stderr

import re


class AccessPoint(__Base):
    def refresh(self):
        try:
            ifconfig = Popen(['ifconfig', self.cfg.get('interface', 'ap0')], stdout=PIPE).stdout.read().decode().rstrip()
            self.ip = self.ip_re.search(ifconfig)
            if self.ip:
                self.ip = self.ip.group(1)
                self.down, self.up = self.downup_re.findall(ifconfig)
                self.down, self.up = self.down.replace('iB', ''), self.up.replace('iB', '')

                params = {
                    'ip': self.ip,
                    'down': self.down,
                    'up': self.up
                }

                self.full_text = self.cfg.get('format', ' %(ip)s  %(down)s  %(up)s') % params
            else:
                self.full_text = self.cfg.get('fail', '')
        except Exception as e:
            print(e, file=stderr)


    def __init__(self, cfg):
        super().__init__(cfg)

        self.downup_re = re.compile('\((\d.+?)\)', re.M)
        self.ip_re = re.compile('inet (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})')
        self.refresh()
