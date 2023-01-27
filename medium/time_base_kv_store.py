class TimeMap:
    """TimeMap keeps a key-value store of the latest value that has been set
    for various keys. A single key can hold many values. Values can be retrieved
    for any timestamp, where the most recent value with a time_stamp <= the inputted
    timestamp is returned."""

    def __init__(self):
        self.tb_store = {} # first try dict with {key: [(timestamp1, value1), (timestamp2,value2)}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # breakpoint()
        if self.tb_store.get(key) is None:
            self.tb_store[key] = [(timestamp, value)]
        else:
            self.tb_store[key].append((timestamp,value))


    def get(self, key: str, timestamp: int) -> str:
        pass

tm = TimeMap()
tm.set("a", "b", 1)
tm.set("a", "z", 4)
tm.set("apple", "zebra", 6)
tm.set("apple", "toast", 7)

print(tm.tb_store)
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

"""
timestamp, key, value
1,          a,      b
2,          a,      c
5,          c,      d
6,          c,      z
8,          a,      k


a: (8,k), (2,c), (1,b)
c: (6,z), (5,d)
"""