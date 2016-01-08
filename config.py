from configparser import ConfigParser


class Config:
    def __init__(self, cfg_name):
        self.config = ConfigParser()
        self.config.read(cfg_name)

    def section(self, sect='DEFAULT'):
        return dict(self.config.items(sect))
