from .base import Base
from subprocess import Popen, PIPE


class Time(Base):
    def __init__(self, cfg):
        super().__init__(cfg)
        hour = int(Popen(['date', '+%H'], stdout=PIPE).stdout.read().decode().rstrip())
        if 0 <= hour < 6:
            self.urgent = True
        self.full_text = Popen(['date', '+'+cfg['format']], stdout=PIPE).stdout.read().decode().rstrip()
