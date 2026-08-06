class Solution:

    def originalDigits(self, s: str) -> str:
        d = {
            "z": 0,
            "w": 2,
            "u": 4,
            "x": 6,
            "g": 8,
            "o": 1,
            "t": 3,
            "f": 5,
            "s": 7,
            "i": 9,
        }
        cnt = [0 for i in range(10)]
        for c in s:
            if c in d:
                cnt[d[c]] += 1
        cnt[1] -= cnt[0] + cnt[2] + cnt[4]
        cnt[3] -= cnt[2] + cnt[8]
        cnt[5] -= cnt[4]
        cnt[7] -= cnt[6]
        cnt[9] -= cnt[5] + cnt[6] + cnt[8]
        return "".join([str(i) * cnt[i] for i in range(10)])
