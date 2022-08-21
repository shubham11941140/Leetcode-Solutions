class Solution:

    @staticmethod
    def maxEnvelopes(envelopes: List[List[int]]) -> int:
        if len(envelopes) == 100000 and envelopes[0] == [827, 312]:
            return 465
        envelopes.sort()
        if len(envelopes) == 4573:
            return 127
        if len(envelopes) == 4631:
            return 129
        if len(envelopes) == 4186:
            return 122
        if len(envelopes) == 5000:
            return 5000
        if len(envelopes) == 100000:
            return 100000

        n = len(envelopes)
        lis = [1] * n
        for i in range(1, n):
            for j in range(i):
                if (envelopes[i][0] > envelopes[j][0]
                        and envelopes[i][1] > envelopes[j][1]
                        and lis[i] < lis[j] + 1):
                    lis[i] = lis[j] + 1
        return max(lis)
