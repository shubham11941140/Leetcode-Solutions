class Solution:

    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        o = [0] * n
        o[0] = pref[0]
        for i in range(1, n):
            o[i] = pref[i] ^ pref[i - 1]
        return o
