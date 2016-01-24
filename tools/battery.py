from .base import Base
from subprocess import Popen, PIPE
import re


class Battery(Base):
    BATTERY = [' ', '_', '▁', '▂', '▃', '▄', '▅', '▆', '▇', '█']

    def __init__(self, cfg):
        Base.__init__(self, cfg['color'])
        ac = Popen(['acpi', '-a'], stdout=PIPE).stdout.read().decode().rstrip()
        acre = re.compile('(on|off)')
        ac = acre.search(ac).group(1)
        if ac == 'off':
            self.urgent = True
            self.full_text = 'AC'
        else:
            bat = Popen(['acpi', '-b'], stdout=PIPE).stdout.read().decode().rstrip()
            batre = re.compile('(\d{1,3})%')
            bat = int(batre.search(bat).group(1))//10
            self.full_text = Battery.BATTERY[bat]
