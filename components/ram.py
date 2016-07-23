from .base import Base
from subprocess import Popen, PIPE
import re


class RAM(Base):
    def __init__(self, cfg):
        super().__init__(cfg)
        self.refresh()

    def refresh(self):
        mem = Popen(['free', '-h', '--si'], stdout=PIPE).stdout
        mem = Popen(['head', '-2'], stdin=mem, stdout=PIPE).stdout
        mem = Popen(['tail', '-1'], stdin=mem, stdout=PIPE).stdout.read().decode().rstrip()

        params_name = ['total', 'used', 'free', 'shared', 'buffers', 'cache', 'available']
        # remove line head and replace ',' to '.' in the memory values
        mems = map(lambda m: m.replace(',', '.'), re.split('\s+', mem)[1:])

        params = dict(zip(params_name, mems))
        self.full_text = self.cfg.get('format', '%(used)s/%(total)s') % params

