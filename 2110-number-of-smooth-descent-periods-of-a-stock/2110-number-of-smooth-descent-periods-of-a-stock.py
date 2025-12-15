class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        x, ans = 1, 0 
        for p1, p2 in pairwise(prices):
            if p2 == p1 - 1:
                x += 1
            else:
                ans += (x * (x + 1)//2)
                x = 1
        return  ans + (x * (x + 1)//2)      