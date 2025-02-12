class Solution:
    def maximumSum(self, nums: List[int]) -> int:    
        digit_sum_map = defaultdict(list)
        for num in nums:
            digit_sum_map[sum(int(digit) for digit in str(num))].append(num)
        max_sum = -1
        for nums_list in digit_sum_map.values():
            if len(nums_list) > 1:
                nums_list.sort(reverse = True)
                max_sum = max(max_sum, nums_list[0] + nums_list[1])
        return max_sum        