from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        res = -1

        if key in self.cache:
            res = self.cache[key]
            self.cache.move_to_end(key, last=True)

        return res

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key, last=True)
            return
        
        if len(self.cache) >= self.capacity:
            # evict
            self.cache.popitem(last=False)
        
        self.cache[key] = value
        self.cache.move_to_end(key, last=True)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)