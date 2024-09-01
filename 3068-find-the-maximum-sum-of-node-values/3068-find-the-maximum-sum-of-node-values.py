class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        max_sum = 0
        changed_count = 0
        min_change_diff = float('inf')
        
        for num in nums:
            max_sum += max(num, num ^ k)
            if (num ^ k) > num:
                changed_count += 1
            min_change_diff = min(min_change_diff, abs(num - (num ^ k)))
        
        if changed_count % 2 == 0:
            return max_sum
        return max_sum - min_change_diff        