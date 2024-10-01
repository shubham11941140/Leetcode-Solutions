class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        r = Counter([((num % k) + k) % k for num in arr])
        for rem in range(k):
            if not rem:
                if r[rem] % 2:
                    return False
            elif r[rem] != r[k - rem]:
                return False
        return True        