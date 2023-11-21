class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num):
            return int(str(num)[::-1])
        
        diff_freq = defaultdict(int)
        for num in nums:
            diff_freq[num - rev(num)] += 1
        
        return sum(f * (f - 1) // 2 for f in diff_freq.values()) % (10**9 + 7)
        