from argparse import ArgumentParser
from sys import exit, stderr

from tools import config


def parse(def_config):
    parser = ArgumentParser(description='Generate status line output for i3bar')
    parser.add_argument('-c', '--config', help='absolute path to the config file', default=def_config)
    args = parser.parse_args()

    if args.config:
        _config = config.config(args.config)
    else:
        parser.print_usage(file=stderr)
        exit(1)

    return _config if _config else None
