from .base import Base
from subprocess import Popen, PIPE, check_call, DEVNULL

import re


class CpuTemp(Base):
    def __init__(self, cfg):
        super().__init__(cfg)
        # check installed lm_sensors
        if check_call('sensors', stdout=DEVNULL) == 0:
            self.command = ['sensors', '-A', 'coretemp-isa-0000']
            self.temp_re = re.compile('Physical id 0:\W{3}(\d{2})')
        # check installed acpi
        elif check_call('acpi', stdout=DEVNULL) == 0:
            self.command = ['acpi', '-t']
            self.temp_re = re.compile('(\d{2})')
        else:
            raise Exception("Not installed acpi or lm_sensors")
        self.refresh()

    def refresh(self):
        self.temp = Popen(self.command, stdout=PIPE).stdout.read().decode().rstrip()
        self.temp = self.temp_re.search(self.temp).group(1)

        if int(self.temp) > int(self.cfg.get('dangerous', '80')):
            self.urgent = True

        params = {
            'temp': self.temp
        }
        self.full_text = self.cfg.get('format', '%(temp)s') % params
