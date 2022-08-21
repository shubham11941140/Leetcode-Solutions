class Solution:
    @staticmethod
    def minCost(colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        i = 0
        ans = 0
        while i < n:
            oi = i
            while i < n - 1 and colors[i] == colors[i + 1]:
                i += 1
            ni = i
            if ni > oi:
                f = neededTime[oi:ni + 1]
                ans += (sum(f) - max(f))
            i += 1
        return ans
