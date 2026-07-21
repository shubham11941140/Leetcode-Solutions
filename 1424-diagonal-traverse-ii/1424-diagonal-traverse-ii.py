class Solution:

    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diagonals[i + j].append(nums[i][j])
        result = []
        for key in sorted(diagonals.keys()):
            result.extend(diagonals[key][::-1])
        return result
