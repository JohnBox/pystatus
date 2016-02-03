from .base import Base
from subprocess import Popen, call, PIPE, DEVNULL
from collections import OrderedDict
import re


class Sound(Base):
    def __init__(self, cfg):
        super().__init__(cfg)
        self.volume_re = re.compile('\[(.*?)\]', re.M)
        if call('amixer', stdout=DEVNULL) == 0:
            self.command = ['amixer', '-c']
        else:
            raise Exception("Not installed amixer")
        self.refresh()

    def refresh(self):
        # check plugged usb sound card
        external = call(['amixer', '-c', '1'], stdout=DEVNULL, stderr=DEVNULL) == 0
        if external:
            card_num = '1'
            master = 'PCM'
        else:
            card_num = '0'
            master = 'Master'

        snd = Popen(['amixer', '-c', card_num], stdout=PIPE, stderr=DEVNULL).stdout.read().decode().strip()
        l = [i.strip() for i in re.split("Simple mixer control '(.*?)',0", snd)]
        d = {k: list(OrderedDict.fromkeys(self.volume_re.findall(v))) for (k, v) in zip(l[1::2], l[2::2])}
        show_icon = self.cfg.get('show_icon', 'False') == 'True'

        icon = ''
        if show_icon:
            if external:
                icon = self.cfg.get('external_icon', '')
            else:
                if '100%' in d['Speaker']:
                    icon = self.cfg.get('speaker_icon', '')
                elif '100%' in d['Headphone']:
                    icon = self.cfg.get('headphone_icon', '')

        if 'on' in d[master]:
            volume = d[master][0][:-1]
        else:
            if show_icon:
                volume = self.cfg.get('mute_icon', '')
            else:
                volume = '__'

        params = {
            'volume': volume,
            'icon': icon
        }
        self.full_text = self.cfg.get('format', '%(volume)s') % params
