class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        return [i for i, v in enumerate(sorted(nums)) if v == target]