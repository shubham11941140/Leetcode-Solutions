class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        def comp(a):
            return abs(a[0] - a[1]) + abs(a[1] - a[2]) + abs(a[2] - a[0])
        d =  defaultdict(list)
        n = len(nums)
        for i in range(n):
            d[nums[i]].append(i)
        if max([len(d[i]) for i in d]) <= 2:
            return -1
        ans = 10 ** 9
        for i in d:
            ldi = len(d[i])
            if ldi > 2:
                ans = min(ans, min([comp(d[i][j:j + 3]) for j in range(ldi - 2)]))
        return ans