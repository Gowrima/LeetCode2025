from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity


    def get(self, key: int) -> int:
        result = -1

        if key in self.cache:
            result = self.cache[key]
            self.cache.move_to_end(key, last=True)
        
        return result

    # cache = [(2,6), (1,2)]
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key, last=True)
            return

        if len(self.cache) >= self.capacity:
            # delete least recent at 0
            self.cache.popitem(last=False)
        
        self.cache[key] = value
        self.cache.move_to_end(key, last=True)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


'''
capacity = 3
put(5, 10)
put(6, 20)
put(7, 30)
get(6)
put(1, 40)

map = {}  # dict[Key: int, Node (pointer to node in Deque)]
{

    6: Node(20)
    7: Node(30)
}

dq = deque()  # value
 <-> Node(30, 7) <-> Node(20, 6)


'''