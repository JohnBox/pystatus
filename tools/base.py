from json import dumps


class Base:
    def __init__(self, cfg):
        self.full_text = '***'
        self.color = cfg.get('color', '#EEEEEE')
        self.urgent = False
        self.separator = True
        self.separator_block_width = 14
        self.visible = True

    def __repr__(self):
        print_fields = ['full_text', 'color', 'urgent', 'separator', 'separator_block_width']
        self.full_text = ' ' + self.full_text + ' '
        obj = {}
        for k in vars(self):
            if k in print_fields:
                obj[k] = self.__dict__[k]
        return dumps(obj)

    def __str__(self):
        return '<{0:s}: "{1:s}">'.format(self.__class__.__name__, self.full_text)
