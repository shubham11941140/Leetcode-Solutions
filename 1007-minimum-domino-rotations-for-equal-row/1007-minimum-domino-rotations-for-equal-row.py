class Solution:

    @staticmethod
    def minDominoRotations(tops: List[int], bottoms: List[int]) -> int:
        ans = 10**10
        for k in range(1, 7):
            c = len([
                i for i in range(len(tops)) if tops[i] != k and bottoms[i] == k
            ])
            if tops.count(k) + c == len(tops):
                ans = min(ans, c)
            c = len([
                i for i in range(len(bottoms))
                if tops[i] == k and bottoms[i] != k
            ])
            if bottoms.count(k) + c == len(bottoms):
                ans = min(ans, c)
        return -1 if ans == 10**10 else ans
