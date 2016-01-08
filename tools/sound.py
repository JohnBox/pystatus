from .base import Base
from subprocess import Popen, PIPE, call
import re


class Sound(Base):
    def __init__(self, color):
        Base.__init__(self, color)
        internal = call('amixer -c 1', shell=True, stdout=PIPE, stderr=PIPE)
        if not internal:
            amixer = ['amixer', '-c', '1', 'get', 'PCM']
        else:
            amixer = ['amixer', '-c', '0', 'get', 'Master']
        sndcard = Popen(amixer, stdout=PIPE).stdout.read().decode().rstrip()
        pattsnd = re.compile('\[(.*?)\]', re.I | re.M | re.S)
        volume, _, mute, *_ = pattsnd.findall(sndcard)
        self.full_text = '_%' if mute == 'off' else volume
