class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = defaultdict(int)
        for i in range(1, n + 1):
            d[sum([int(j) for j in str(i)])] += 1
        m = max(d.values())
        return len([i for i in d if d[i] == m])        