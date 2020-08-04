class RingBuffer:
    def __init__(self, capacity):
        #max compacity
        self.capacity = capacity
        #storage
        self.data = []
        self.count = 0

    def append(self, item):
        if len(self.data) < self.capacity:
            print(item)
            self.data.append(item)
            print(self.data)

        else:
            print(item)
            #remove first element
            self.data.pop(0)
            #insert the
            self.data.insert(self.count, item)
                self.count += 1
            print(self.data)
    def get(self):

        return self.data
