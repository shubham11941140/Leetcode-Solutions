class Solution:

    @staticmethod
    def searchRange(nums: List[int], target: int) -> List[int]:
        ans = []
        for i, item in enumerate(nums):
            if item == target:
                ans.append(i)
        if not ans:
            return [-1, -1]
        return [ans[0], ans[-1]]
