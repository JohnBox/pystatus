from .base import Base
from subprocess import Popen, PIPE, call, DEVNULL

import re


class CpuFan(Base):
    def __init__(self, cfg):
        super().__init__(cfg)
        # check installed lm_sensors
        if call('sensors', stdout=DEVNULL) == 0:
            self.command = ['sensors', '-A']
            chip = self.cfg.get('chip', '')
            if chip:
                self.command.append(chip)
            self.fan_re = re.compile('cpu_fan:\s+(.*) RPM')
        else:
            raise Exception("Not installed lm_sensors")
        self.refresh()

    def refresh(self):
        self.fan = Popen(self.command, stdout=PIPE).stdout.read().decode().rstrip()
        self.fan = self.fan_re.search(self.fan).group(1)
        if self.cfg.get('show_thousand', 'False') == 'True':
            self.fan = str(int(self.fan) / 1000) + 'K'

        params = {
            'rpm': self.fan
        }
        self.full_text = self.cfg.get('format', '%(rpm)s') % params
