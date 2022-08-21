class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

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

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            s = set()
            for i, item in enumerate(nums):
                if (
                    len(res) == 0
                    or res[-1][1] != item
                    and target - item in s
                ):
                    res.append([target - item, item])
                s.add(item)
            return res

        nums.sort()
        return kSum(nums, target, 4)
