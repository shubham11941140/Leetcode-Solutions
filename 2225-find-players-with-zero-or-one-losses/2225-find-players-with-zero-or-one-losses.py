class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        t = []
        for i in matches:
            t += i
        t = set(t)
        l = Counter([y for [x, y] in matches])
        return [
            sorted([i for i in t if i not in l]),
            sorted([i for i in l if l[i] == 1]),
        ]
