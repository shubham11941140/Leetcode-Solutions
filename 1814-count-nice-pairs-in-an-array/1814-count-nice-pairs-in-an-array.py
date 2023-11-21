class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num):
            return int(str(num)[::-1])
        
        d = defaultdict(int)
        for num in nums:
            d[num - rev(num)] += 1
        
        return sum(f * (f - 1) // 2 for f in d.values()) % (10**9 + 7)
        