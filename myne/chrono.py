import time


class Chrono:
    def __init__(self):
        self._start = time.time()

    # Magics

    def __str__(self):
        return f"Chrono({round(self.get(), 5)} sec)"

    def __repr__(self):
        return str(self)

    def __gt__(self, value):
        return self.get() > value

    def __ge__(self, value):
        return self.get() >= value

    def __lt__(self, value):
        return self.get() < value

    def __le__(self, value):
        return self.get() <= value
       
    # Properties

    @property
    def seconds(self) -> float:
        return self.get()

    @property
    def minutes(self) -> float:
        return self.seconds / 60

    @property
    def hours(self) -> float:
        return self.minutes / 60

    @property
    def clock(self) -> str:
        m, s = divmod(self.get(), 60)
        h, m = divmod(m, 60)
        return f"{h:02.0f}:{m:02.0f}:{s:06.3f}"

    # Methods

    def start(self):
        self._start = time.time()

    def reset(self):
        self._start = time.time()

    def get(self) -> float:
        return time.time() - self._start

    def delta(self) -> float:
        t = self.get()
        self.reset()
        return t

    def turn_is(self, t:float) -> bool:
        if self.get() > t:
            self.reset()
            return True
        else:
            return False


if __name__ == '__main__':
    # c = Chrono()
    # print("Get:", c.get())
    # print(c, "> 3 =", c > 3)
    # print(c, ">= 3 =", c >= 3)
    # print(c, "< 10 =", c < 10)
    # print(c, "<= 10 =", c <= 10)
    # print("Sleep 3 seconds")
    # time.sleep(3)
    # print(c, ">= 3 =", c >= 3)
    # c.reset()
    # print("Reset", c)

    # print("Sleep 3 seconds")
    # time.sleep(3)
    # val = c.delta()
    # print("Delta", val, c)

    # print("While turn_is 3 sec")
    # while not c.turn_is(3):
    #     pass
    # print(c)

    c = Chrono()
    time.sleep(2)
    print("Clock")
    print(c)
    print(c.clock)
