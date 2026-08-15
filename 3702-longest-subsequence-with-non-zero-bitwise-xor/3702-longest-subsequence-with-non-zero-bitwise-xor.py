class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        oddCountFound = False
        allZeros = True
        for bit in range(32):
            oneCount = 0
            for num in nums:
                if (num >> bit) & 1:
                    oneCount += 1

                if bit == 0 and num:
                    allZeros = False

            if oneCount % 2:
                oddCountFound = True
                break

        if allZeros:
            return 0

        return len(nums) + (0 if oddCountFound else -1)        