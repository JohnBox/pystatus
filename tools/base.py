from json import dumps


class Base:
    def __init__(self, color, urgent=None):
        self.full_text = ' *** '
        self.color = color
        self.urgent = urgent
        # self.min_width = 100
        self.separator = False
        self.separator_block_width = 29

    def __str__(self):
        return dumps(self.__dict__)

    def __repr__(self):
        return dumps(self.__dict__)
