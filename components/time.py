from .base import Base
from locale import setlocale, LC_TIME
from datetime import datetime


class Time(Base):
    def __init__(self, cfg):
        super().__init__(cfg)
        setlocale(LC_TIME, 'uk_UA')
        hour = datetime.now().strftime('%H')
        if int(cfg['sleep']) <= int(hour) < int(cfg['wakeup']):
            self.urgent = True
        self.full_text = datetime.now().strftime(cfg['format'])
