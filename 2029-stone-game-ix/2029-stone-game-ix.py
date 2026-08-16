class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = Counter(x % 3 for x in stones)
        return abs(cnt[1] - cnt[2]) > 2 if cnt[0] % 2 else min(cnt[1], cnt[2]) > 0