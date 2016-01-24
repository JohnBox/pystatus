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
        bat = Popen(['acpi', '-b'], stdout=PIPE).stdout.read().decode().rstrip()
        batre = re.compile('(\d{1,3})%')
        bat = int(batre.search(bat).group(1))
        bat = bat-1 if bat else bat
        self.full_text = Battery.BATTERY[bat//len(Battery.BATTERY)]
