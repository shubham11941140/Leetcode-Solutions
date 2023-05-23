from random import choice


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        a = [[] for i in range(10)]
        a[2] = list("abc")
        a[3] = list("def")
        a[4] = list("ghi")
        a[5] = list("jkl")
        a[6] = list("mno")
        a[7] = list("pqrs")
        a[8] = list("tuv")
        a[9] = list("wxyz")
        d = [int(i) for i in digits]
        ans = []
        for _ in range(1000):
            v = "".join([choice(a[i]) for i in d])
            ans.append(v)
        return set(ans)
