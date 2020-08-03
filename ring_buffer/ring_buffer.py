class RingBuffer:
    def __init__(self, capacity):
        self.capacty = capacity
        self.data = []
    class __Full:

        def append(self, item):
            self.data[self.cur] = item
            self.cur = (self.cur+1) % self.max

    def get(self):
        pass
