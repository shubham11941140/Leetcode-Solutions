class Solution:

    def __init__(self):
        self.c = 0
        self.a = ["a", "e", "i", "o", "u"][::-1]

    def pall(self, b, k):
        if not k:
            self.c += 1
            return
        else:
            for i in self.a:
                if b != -1:
                    if i < b:
                        break
                    else:
                        self.pall(i, k - 1)
                else:
                    self.pall(i, k - 1)

    def countVowelStrings(self, n: int) -> int:
        self.pall(-1, n)
        return self.c
