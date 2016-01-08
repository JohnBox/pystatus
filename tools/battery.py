from .base import Base
from subprocess import Popen, PIPE
import re


class Battery(Base):
    BATTERY = [' ', '_', '▁', '▂', '▃', '▄', '▅', '▆', '▇', '█']

    def __init__(self, cfg):
        Base.__init__(self, cfg['color'])
        bat = Popen(['acpi', '-b'], stdout=PIPE).stdout.read().decode().rstrip()
        pattbat = re.compile('(\d{1,3})%')
        bat = int(pattbat.findall(bat)[0])//10
        self.full_text = Battery.BATTERY[bat]
