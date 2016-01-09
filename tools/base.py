from json import dumps


class Base:
    def __init__(self, color='#EEEEEE', urgent=None):
        self.full_text = '***'
        self.color = color
        self.urgent = urgent
        # self.min_width = 100
        self.separator = True
        self.separator_block_width = 14

    def __str__(self):
        self.full_text = ' ' + self.full_text + ' '
        return dumps(self.__dict__)

    def __repr__(self):
        self.full_text = ' ' + self.full_text + ' '
        return dumps(self.__dict__)
