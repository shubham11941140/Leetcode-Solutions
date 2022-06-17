class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # Get intervals and then remove
        n = len(colors)
        i = 0
        r = []
        while i < n:
            oi = i
            while i < n - 1 and colors[i] == colors[i + 1]:
                i += 1
            ni = i
            if ni > oi:
                r.append((oi, ni))
            i += 1
        ans = 0
        for oi, ni in r:
            f = neededTime[oi:ni + 1]
            ans += (sum(f) - max(f))
        return ans
        