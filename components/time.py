from .base import Base
from locale import setlocale, LC_TIME
from datetime import datetime


class Time(Base):
    def __init__(self, cfg):
        super().__init__(cfg)
        setlocale(LC_TIME, 'uk_UA')
        self.refresh()

    def refresh(self):
        hour = datetime.now().strftime('%H')
        if int(self.cfg.get('sleep', '0')) <= int(hour) < int(self.cfg.get('wakeup', '6')):
            self.urgent = True
        self.full_text = datetime.now().strftime(self.cfg.get('format', '%R'))
