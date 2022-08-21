class Solution:

    @staticmethod
    def fourSum(nums: List[int], target: int) -> List[List[int]]:

        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []
            if not nums:
                return res
            average_value = target // k
            if average_value < nums[0] or nums[-1] < average_value:
                return res
            if k == 2:
                return twoSum(nums, target)
            for i, item in enumerate(nums):
                if i == 0 or nums[i - 1] != item:
                    for subset in kSum(nums[i + 1:], target - item, k - 1):
                        res.append([item] + subset)

            return res

        nums.sort()
        return kSum(nums, target, 4)
