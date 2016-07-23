from .base import Base
from datetime import datetime


class Time(Base):
    def __init__(self, cfg):
        super().__init__(cfg)
        self.refresh()

    def refresh(self):
        hour = datetime.now().strftime('%H')
        self.full_text = datetime.now().strftime(self.cfg.get('format', '%R'))
        if int(self.cfg.get('sleep', '0')) <= int(hour) < int(self.cfg.get('wakeup', '6')):
            self.urgent = True
            self._text += '  '
        else:
            self.urgent = False
