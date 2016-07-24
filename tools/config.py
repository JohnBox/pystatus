from argparse import ArgumentParser
from configparser import ConfigParser
import os
import sys


def parse():
    # default config location pystatus/pystatus.ini
    parser = ArgumentParser(description='Generate status line output for i3bar')
    parser.add_argument('-c', '--config',
                        help='path to the config file',
                        default='pystatus.ini')
    args = parser.parse_args()
    config_path = os.path.abspath(args.config)
    if os.path.exists(config_path):
        config = ConfigParser()
        config.read(config_path)
        return config
    else:
        print('%s not exists' % config_path, file=sys.stderr)
        parser.print_usage(file=sys.stderr)
        exit(1)
