class WordFilter:

    def __init__(self, words: List[str]):
        # Create a word index
        self.n = len(words)
        self.c = set()
        self.words = []
        self.revwords = []
        for i in reversed(range(self.n)):
            if words[i] not in self.c:
                self.c.add(words[i])
                self.words.append([words[i], i])
                self.revwords.append([words[i][::-1], i])
        self.newn = len(self.words)

    def f(self, prefix: str, suffix: str) -> int:        
        revsuffix = suffix[::-1]
        lenpre = len(prefix)
        lensuf = len(suffix)
        for i in range(self.newn):
            if self.words[i][0][:lenpre] == prefix and self.revwords[i][0][:lensuf] == revsuffix:
                return self.words[i][1]
        return -1                                    

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)