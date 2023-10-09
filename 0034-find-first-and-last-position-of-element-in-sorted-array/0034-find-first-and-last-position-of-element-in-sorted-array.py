class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [i for i in range(len(nums)) if nums[i] == target]
        return [-1, -1] if not ans else [ans[0], ans[-1]]
       