from .base import Base
from subprocess import Popen, PIPE
import re


class CpuTemp(Base):
    def __init__(self, cfg):
        Base.__init__(self, cfg['color'])
        temp = Popen(['acpi', '-t'], stdout=PIPE).stdout.read().decode().rstrip()
        tempre = re.compile('(\d{2})')
        temp = tempre.search(temp).group(1)
        if int(temp) > int(cfg['dangerous']):
            self.urgent = True
        self.full_text = '%(temp)s°C' % locals()
