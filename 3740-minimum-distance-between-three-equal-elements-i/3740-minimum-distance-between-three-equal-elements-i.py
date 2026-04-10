class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        def compute(a):
            return abs(a[0] - a[1]) + abs(a[1] - a[2]) + abs(a[2] - a[0])
        d = defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)
        print(d)
        if max([len(d[i]) for i in d]) <= 2:
            return -1
        ans = 10 ** 9
        for i in d:
            di = d[i]
            if len(di) > 2:
                for j in range(len(di) - 2):
                    ans = min(ans, compute(di[j:j + 3]))
        return ans
