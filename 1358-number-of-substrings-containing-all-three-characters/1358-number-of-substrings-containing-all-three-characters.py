class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lastA = lastB = lastC = -1
        total = 0
        for i, ch in enumerate(s):
            if ch == 'a':
                lastA = i
            elif ch == 'b':
                lastB = i
            else:
                lastC = i
            if min(lastA, lastB, lastC) != -1:
                total += min(lastA, lastB, lastC) + 1
        return total