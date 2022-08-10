class MapSum:

    def __init__(self):
        self.d = {}
        

    def insert(self, key: str, val: int) -> None:
        self.d[key] = val
                    
    def sum(self, prefix: str) -> int:
        n = len(prefix)
        ans = 0
        for i in self.d:
            if i[:n] == prefix:
                ans += self.d[i]
        return ans
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)