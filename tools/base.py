from json import dumps


class Base:
    def __init__(self, color):
        self.full_text = ' *** '
        self.color = color
        self.urgent = None

    def __str__(self):
        return dumps(self.__dict__)

    def __repr__(self):
        return dumps(self.__dict__)
