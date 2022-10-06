from collections import defaultdict
from bisect import bisect

class TimeMap:

    def __init__(self):
        self.t = defaultdict(list)
                
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.t[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        i = bisect(self.t[key], (timestamp, chr(127)))
        return self.t[key][i - 1][1] if i else ""                            

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)