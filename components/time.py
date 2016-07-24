from .base import Base as __Base
from datetime import datetime


class Time(__Base):
    def __init__(self, cfg):
        super().__init__(cfg)
        self.refresh()

    def refresh(self):
        hour = datetime.now().strftime('%H')
        self.full_text = datetime.now().strftime(self.cfg.get('format', '%d/%m %R'))
        if int(self.cfg.get('sleep', '0')) <= int(hour) < int(self.cfg.get('wakeup', '6')):
            self.urgent = True
            self.full_text += '  '
        else:
            self.urgent = False
