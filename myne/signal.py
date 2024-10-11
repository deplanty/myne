

class Signal:
    def __init__(self):
        self._funcs = list()

    def connect(self, func):
        self._funcs.append(func)

    def disconnect(self, *funcs):
        for func in funcs:
            try:
                self._funcs.remove(func)
            except:
                pass

    def emit(self):
        for func in self._funcs:
            func()
