from .base import Base
from subprocess import Popen, PIPE, call
import re


class Sound(Base):
    def __init__(self, cfg):
        Base.__init__(self, cfg['color'])
        internal = call('amixer -c 1', shell=True, stdout=PIPE, stderr=PIPE)
        if not internal:
            amixer = ['amixer', '-c', '1', 'get', 'PCM']
        else:
            amixer = ['amixer', '-c', '0', 'get', 'Master']
        sndcard = Popen(amixer, stdout=PIPE).stdout.read().decode().rstrip()
        sndre = re.compile('\[(.*?)\]', re.M)
        volume, _, mute, *_ = sndre.findall(sndcard)
        self.full_text = '__' if mute == 'off' else '%(volume)s' % locals()
