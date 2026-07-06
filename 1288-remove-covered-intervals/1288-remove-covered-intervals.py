class Solution:    
    def removeCoveredIntervals(self, it: List[List[int]]) -> int:
        it.sort()
        while True:
            cur = len(it)
            for i in range(len(it) - 1):
                if it[i][0] <= it[i + 1][0] and it[i + 1][1] <= it[i][1]:
                    it.remove(it[i + 1])
                    break
                elif it[i][0] >= it[i + 1][0] and it[i + 1][1] >= it[i][1]:
                    it.remove(it[i])
                    break
            nex = len(it)
            if cur == nex:
                break
        return len(it)                                    