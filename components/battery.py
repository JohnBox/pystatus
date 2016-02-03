from .base import Base
from subprocess import Popen, PIPE

import re
import string


class Battery(Base):
    BATTERY = ['', '', '', '', '']

    def __init__(self, cfg):
        super().__init__(cfg)
        self.visible = not (cfg.get('show_ac', 'False') == 'True')
        self.ac_re = re.compile('(on|off)')
        self.refresh()

    def refresh(self):
        self.ac = Popen(['acpi', '-a'], stdout=PIPE).stdout.read().decode().rstrip()
        self.ac = self.ac_re.search(self.ac).group(1)

        show_only_ac = self.cfg.get('show_only_ac', 'False') == 'True'
        if show_only_ac:
            if self.ac == 'off':
                self.urgent = True
                self.visible = True
                self.full_text = ''
            else:
                self.urgent = False
                self.visible = False
        else:
            self.battery = Popen('acpi', stdout=PIPE).stdout.read().decode().rstrip()
            # remove line head and split battery values
            self.battery = [i.strip() for i in re.sub('Battery \d: ', '', self.battery).split(',')]
            self.status, self.capacity = self.battery[:2]

            # remove last percent symbol
            self.capacity = int(self.capacity[:-1])
            if self.cfg.get('show_icon', 'False') == 'True':
                self.capacity //= 20
                self.capacity -= 1 if self.capacity > 0 else 0
                self.capacity = Battery.BATTERY[self.capacity]

            self.battery = self.battery[2:]
            # has time of charging or discharging
            if self.battery:
                # stay only time
                self.time = self.battery[0].split()[0]
            else:
                self.time = ''

            params = {
                'status': self.status,
                'capacity': self.capacity,
                'time': self.time,
                'ac': self.ac
            }

            self.full_text = self.cfg.get('format', '%(ac)s') % params

            if self.ac == 'off':
                self.urgent = True
                self.full_text = ''
            else:
                self.urgent = False







