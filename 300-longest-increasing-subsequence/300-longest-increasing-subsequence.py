from bisect import bisect_left
class Solution:    
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        tail = [0 for i in range(n + 1)]
        length = 1

        tail[0] = nums[0]

        for i in range(1, n):
            if nums[i] > tail[length-1]:
                tail[length] = nums[i]
                length += 1
            else:
                tail[bisect_left(tail, nums[i], 0, length-1)] = nums[i]

        return length        
                
        