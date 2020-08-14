class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest_data = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.oldest_data] = item
            if self.oldest_data < len(self.storage) - 1:
                self.oldest_data += 1
            else:
                self.oldest_data = 0


        #     # Check which item is the oldest
        #     if self.oldest_data < len(self.storage -1):
        #         self.oldest_data += 1
        #     else:
        #         self.oldest_data = 0 
        # elif len(self.storage) < self.capacity:
        #     self.storage[self.oldest_data] = item


    def get(self):
        return self.storage 