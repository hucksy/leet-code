from collections import OrderedDict

class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self:
            self.move_to_end(key, last=False) #moves this key to the beginning
        return self.get(key, -1)

    def put(self, key: int, val: int) -> None:
            self[key] = val
            self.move_to_end(key, last=False)
            if len(self) > self.capacity:
                self.popitem(last=True)

from collections import OrderedDict

c = LRUCache(3)
c.put(1,2)
c.put(6,3)
c.put(7,2)
print(c)
c.put(8,6)
print(c)
c.put(6,99)
print(c)