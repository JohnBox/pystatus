from json import dumps


class Base:

    def __init__(self, cfg):
        self.cfg = cfg
        self.full_text = '***'
        self.short_text = '*'
        self.color = cfg.get('color', '#EEEEEE')
        self.background = '#666666'
        self.border = '#FFFFFF'
        self.min_width = 10
        self.align = 'center'
        self.urgent = False
        self.separator = True
        self.separator_block_width = 9
        self.markup = 'none'
        self.visible = True

    def __str__(self):
        print_fields = [
            'full_text',
            'color',
            'background',
            'border',
            'urgent',
            'separator',
            'separator_block_width'
        ]
        obj = {}
        for k in print_fields:
            if k in ['full_text']:
                obj[k] = '\u00A0' + getattr(self, k) + '\u00A0'
            else:
                obj[k] = getattr(self, k)
        return dumps(obj)

    def __repr__(self):
        return self.__str__()
