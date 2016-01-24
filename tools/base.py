from json import dumps


class Base:
    def __init__(self, color='#EEEEEE'):
        self.full_text = '***'
        self.color = color
        self.urgent = False
        self.separator = True
        self.separator_block_width = 14

    def __str__(self):
        self.full_text = ' ' + self.full_text + ' '
        return dumps(vars(self))

    def __repr__(self):
        self.full_text = ' ' + self.full_text + ' '
        return dumps(vars(self))
