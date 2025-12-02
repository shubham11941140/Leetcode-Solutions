class Solution:

    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = int(10**9 + 7)

        freq_dict = Counter([p[1] for p in points])

        for y, freq in freq_dict.items():
            freq_dict[y] = comb(freq, 2)

        ans = 0
        ps = 0

        for e in freq_dict.values():
            ans = (ans + e * ps) % mod
            ps = (ps + e) % mod

        return ans
