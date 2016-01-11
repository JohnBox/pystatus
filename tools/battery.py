from .base import Base
from subprocess import Popen, PIPE
import re


class Battery(Base):
    BATTERY = [' ', '_', '▁', '▂', '▃', '▄', '▅', '▆', '▇', '█']

    def __init__(self, cfg):
        Base.__init__(self, cfg['color'])
        bat = Popen(['acpi', '-b'], stdout=PIPE).stdout.read().decode().rstrip()
        batre = re.compile('(\d{1,3})%')
        bat = int(batre.search(bat).group(1))//10-1
        self.full_text = Battery.BATTERY[bat]
