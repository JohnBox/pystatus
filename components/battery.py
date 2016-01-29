from .base import Base
from subprocess import Popen, PIPE
import re


class Battery(Base):

    def __init__(self, cfg):
        Base.__init__(self, cfg['color'])
        ac = Popen(['acpi', '-a'], stdout=PIPE).stdout.read().decode().rstrip()
        acre = re.compile('(on|off)')
        self.ac = acre.search(ac).group(1)
        if self.ac == 'off':
            self.urgent = True
            self.full_text = 'AC'
