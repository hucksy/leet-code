# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class LRUCache:
    lru_count = 0
    cache = {}

    """
    # cache needs to allow o(1) get and put...dictionary should do that

    {key:{
        value: val, 
        tick: t}}   # tick will be counter to measure expulsion, increments with each get/put, min value is expelled
    """

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.lru_count += 1
            self.cache[key]["tick"] = self.lru_count
        rec = self.cache.get(key, -1)
        if rec == -1:
            return rec
        else:
            return rec["value"]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.lru_count += 1
            self.cache.update({key:{'value': value, 'tick': self.lru_count}})
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                min_tick = 10 ** 8
                expel_key = -1
                for i, rec in enumerate(self.cache):
                    if self.cache[rec]["tick"] < min_tick:
                        min_tick = self.cache[rec]["tick"]
                        expel_key = rec
                self.cache.pop(expel_key)
            self.cache.update({key:{'value': value, 'tick': self.lru_count}})


obj = LRUCache(capacity=2)
obj.put(1, 0)
obj.put(2, 2)
print(obj.get(1))
obj.put(3,3)
print(obj.get(2))
obj.put(4,4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))

"""
["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],       [1,0],[2,2],[1],   [3,3],[2], [4,4],[1],   [3],  [4]]
"""