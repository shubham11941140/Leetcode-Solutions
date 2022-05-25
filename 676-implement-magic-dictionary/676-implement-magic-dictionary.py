class MagicDictionary:

    def __init__(self):
        self.a = []
        
    def diff(self, a, b):
        if len(a) == len(b):
            n = len(a)
            l = len([1 for i in range(n) if a[i] != b[i]])
            return True if l == 1 else False
        else:
            return False
    
    def buildDict(self, dictionary: List[str]) -> None:
        self.a = [i for i in dictionary]
        
    def search(self, searchWord: str) -> bool:
        for i in self.a:
            if self.diff(searchWord, i):
                return True
        return False
        
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)