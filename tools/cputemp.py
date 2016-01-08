from .base import Base
from subprocess import Popen, PIPE
import re


class CpuTemp(Base):
    def __init__(self, cfg):
        Base.__init__(self, cfg['color'])
        temp = Popen(['acpi', '-t'], stdout=PIPE).stdout.read().decode().rstrip()
        pattemp = re.compile('.*ok, (\d{2})')
        temp = pattemp.findall(temp)[0]
        if int(temp) > int(cfg['dangerous']):
            self.urgent = True
        self.full_text = '%s°C' % temp
