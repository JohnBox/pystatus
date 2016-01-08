from .base import Base
from subprocess import Popen, PIPE


class Time(Base):
    def __init__(self, color, format='%d/%m %R'):
        Base.__init__(self, color)
        hour = int(Popen(['date', '+%H'], stdout=PIPE).stdout.read().decode().rstrip())
        if 0 < hour < 6:
            self.urgent = True
        self.full_text = Popen(['date', '+'+format], stdout=PIPE).stdout.read().decode().rstrip()