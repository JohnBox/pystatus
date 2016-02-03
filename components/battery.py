from .base import Base
from subprocess import Popen, call, PIPE, DEVNULL
from collections import namedtuple

import re
import string


class Battery(Base):
    BATTERY = ['', '', '', '', '']

    def __init__(self, cfg):
        super().__init__(cfg)
        if call('acpi', stdout=DEVNULL, stderr=DEVNULL) != 0:
            raise Exception('Not installed acpi')
        self.visible = not (cfg.get('show_ac', 'False') == 'True')
        self.ac_re = re.compile('(on|off)')
        self.Battery = namedtuple('Battery', 'state, capacity, time')
        self.refresh()

    def _create_battery(self, battery_str):
        battery = [i.strip() for i in re.sub('Battery \d: ', '', battery_str).split(',')]
        # add empty time if not exist
        if len(battery) == 2:
            battery.append('')
        battery = self.Battery._make(battery)
        # remove last percent symbol from capacity
        capacity = int(battery.capacity[:-1])
        # stay only time
        time = battery.time.split()
        time = time[0] if time else ''
        battery = battery._replace(capacity=capacity, time=time)
        return battery

    def refresh(self):
        self.ac = Popen(['acpi', '-a'], stdout=PIPE).stdout.read().decode().rstrip()
        self.ac = self.ac_re.search(self.ac).group(1)

        show_only_ac = self.cfg.get('show_only_ac', 'False') == 'True'
        if show_only_ac:
            if self.ac == 'off':
                self.visible = True
                self.full_text = ''
            else:
                self.visible = False
        else:
            self.battery = Popen('acpi', stdout=PIPE).stdout.read().decode().rstrip()
            self.battery = self._create_battery(self.battery)

            if self.cfg.get('show_icon', 'False') == 'True':
                capacity = self.battery.capacity // 20
                capacity -= 1 if capacity > 0 else 0
                self.battery = self.battery._replace(capacity=Battery.BATTERY[capacity])

            params = {
                'state': self.battery.state,
                'capacity': self.battery.capacity,
                'time': self.battery.time,
                'ac': self.ac
            }

            self.full_text = self.cfg.get('format', '%(ac)s') % params

        if self.ac == 'off':
            self.urgent = True
        else:
            self.urgent = False
