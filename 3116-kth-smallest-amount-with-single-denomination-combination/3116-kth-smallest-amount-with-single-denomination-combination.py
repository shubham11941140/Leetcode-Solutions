class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        dic = defaultdict(list)
        for i in range(1, n + 1):
            for comb in itertools.combinations(coins, i):
                dic[len(comb)].append(math.lcm(*comb))
        
        def count(dic, target):
            return sum([sum([(target // lcm * pow(-1, i + 1)) for lcm in dic[i]]) for i in range(1, n + 1)])
        
        start, end = min(coins), min(coins) * k
        while start + 1 < end:
            mid = (start + end) // 2
            if count(dic, mid) >= k:
                end = mid
            else:
                start = mid
        return start if count(dic, start) >= k else end