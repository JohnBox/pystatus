from configparser import ConfigParser

import os.path


def config(config_file):
    _config = ConfigParser()
    _config.read(os.path.abspath(config_file))
    return _config if _config else None
