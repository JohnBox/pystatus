from json import dumps


class Base:
    @property
    def full_text(self):
        return ' ' + self.text + ' '

    @full_text.setter
    def full_text(self, value):
        self.text = value

    def __init__(self, cfg):
        self.cfg = cfg
        self.text = '***'
        self.color = cfg.get('color', '#0C99D5')
        self.urgent = False
        self.separator = True
        self.separator_block_width = 9
        self.visible = True

    def __str__(self):
        print_fields = ['full_text', 'color', 'urgent', 'separator', 'separator_block_width']
        obj = {}
        for k in print_fields:
            obj[k] = getattr(self, k)
        return dumps(obj)

    def __repr__(self):
        return self.__str__()
        # return '<{0:s}: "{1:s}">'.format(self.__class__.__name__, self.full_text)
