class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a = [0]
        for i in gain:
            a.append(a[-1] + i)
        print(a)
        return max(a)
        