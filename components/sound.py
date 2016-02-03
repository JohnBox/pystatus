from .base import Base
from subprocess import Popen, check_call, PIPE, DEVNULL
from collections import OrderedDict
import re
from time import time


class Sound(Base):
    def __init__(self, cfg):
        super().__init__(cfg)
        self.volume_re = re.compile('\[(.*?)\]', re.M)
        self.command = ['amixer', '-c', '0']
        self.refresh()

    def refresh(self):
        start = time()
        # check plugged usb sound card
        # external = check_call(['amixer', '-c', '1'], stdout=DEVNULL, stderr=DEVNULL, shell=True) == 0

        snd = Popen(self.command, stdout=PIPE).stdout.read().decode().strip()

        l = [i.strip() for i in re.split("Simple mixer control '(.*?)',0", snd)]
        d = {k: list(OrderedDict.fromkeys(self.volume_re.findall(v))) for (k, v) in zip(l[1::2], l[2::2])}

        icon = ''
        volume = d['Master'][0][:-1]
        show_icon = self.cfg.get('show_icon', 'False') == 'True'
        if show_icon:
            if 'on' in d['Speaker']:
                icon = self.cfg.get('speaker_icon', '')
            elif 'on' in d['Headphone']:
                icon = self.cfg.get('headphone_icon', '')
            elif 'off' in d['Master']:
                icon = self.cfg.get('mute_icon', '')
                volume = ''

        params = {
            'volume': volume,
            'icon': icon
        }
        self.full_text = self.cfg.get('format', '%(volume)s') % params
