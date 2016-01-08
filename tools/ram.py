from .base import Base
from subprocess import Popen, PIPE
import re


class RAM(Base):
    def __init__(self, cfg):
        Base.__init__(self, cfg['color'])
        mem = Popen(['free', '-h', '--si'], stdout=PIPE).stdout
        mem = Popen(['head', '-2'], stdin=mem, stdout=PIPE).stdout
        mem = Popen(['tail', '-1'], stdin=mem, stdout=PIPE).stdout.read().decode().rstrip()
        mem = list(filter(bool, mem.split()))[2]
        self.full_text = mem

