#!/usr/bin/env python3
import components
from tools import config as config_parser
from json import dumps
from sys import stdout
import time


def main():
    config = config_parser.parse()
    VERSION = {'version': 1}
    print(dumps(VERSION))
    print('[')
    interval = float(config['PYSTATUS'].get('refresh', 1.0))
    components_cfg = config.sections()[:]
    components_cfg.remove('PYSTATUS')
    panel = []
    for cfg in components_cfg:
        try:
            component = getattr(components, cfg.upper())
            panel.append(component(config[cfg]))
        except:
            pass
    panel.reverse()
    while True:
        start = time.time()
        visibled = list(filter(lambda i: i.visible, panel))
        print(visibled, end=',\n')
        map(lambda i: i.refresh(), panel)
        late = time.time() - start
        time.sleep((interval - late) if (interval - late) > 0 else interval)
        stdout.flush()

if __name__ == '__main__':
    main()

