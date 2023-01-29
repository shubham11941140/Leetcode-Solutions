class LFUCache:

        def __init__(self, capacity: int):
            self.capacity = capacity
            self.cache = {}
            self.freq = defaultdict(OrderedDict)
            self.min_freq = 0
    
        def get(self, key: int) -> int:
            if key not in self.cache:
                return -1
            val, freq = self.cache[key]
            self.freq[freq].pop(key)
            if not self.freq[freq]:
                del self.freq[freq]
                if self.min_freq == freq:
                    self.min_freq += 1
            self.freq[freq + 1][key] = val
            self.cache[key] = (val, freq + 1)
            return val
    
        def put(self, key: int, value: int) -> None:
            if not self.capacity:
                return
            if key in self.cache:
                self.cache[key] = (value, self.cache[key][1])
                self.get(key)
                return
            if len(self.cache) == self.capacity:
                k, v = self.freq[self.min_freq].popitem(last=False)
                del self.cache[k]
            self.cache[key] = (value, 1)
            self.freq[1][key] = value
            self.min_freq = 1       


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)