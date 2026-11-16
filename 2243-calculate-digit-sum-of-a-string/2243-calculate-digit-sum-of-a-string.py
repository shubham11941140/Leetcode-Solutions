class Solution:
    def digitSum(self, s: str, k: int) -> str:
        return s if len(s) <= k else self.digitSum(''.join(str(sum(map(int, g))) for g in batched(s, k)), k)