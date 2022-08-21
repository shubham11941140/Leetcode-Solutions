class Solution:

    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        g = sorted(nums)[::-1][:k]
        n = []
        for i in nums:
            if i in g:
                n.append(i)
                g.remove(i)
        return n
