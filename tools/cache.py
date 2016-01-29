

class Cache:
    def __init__(self, times):
        self.times = times
        self.n = 0

    def __call__(self, f):
        def wrap(*args):
            if self.n == 0:
                f(*args)
                self.n = self.times
            else:
                self.n -= 1

        return wrap
