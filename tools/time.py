from .base import Base
from subprocess import Popen, PIPE


class Time(Base):
    def __init__(self, cfg):
        super().__init__(cfg)
        hour = Popen(['date', '+%H'], stdout=PIPE).stdout.read().decode().rstrip()
        if int(cfg['sleep']) <= int(hour) < int(cfg['wakeup']):
            self.urgent = True
        self.full_text = Popen(['date', '+'+cfg['format']], stdout=PIPE).stdout.read().decode().rstrip()
