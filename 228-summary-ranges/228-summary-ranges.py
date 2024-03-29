class Solution:

    @staticmethod
    def summaryRanges(nums: List[int]) -> List[str]:
        n = len(nums)
        i = 0
        ans = []
        while i < n:
            curr = nums[i]
            while i < n - 1 and nums[i + 1] == nums[i] + 1:
                i += 1
            nex = nums[i]
            if curr == nex:
                ans.append(str(curr))
            else:
                ans.append(str(curr) + "->" + str(nex))
            i += 1
        return ans
