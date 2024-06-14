class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        A = sorted(nums)
        move = 0
        for i in range(1, len(A)):
            if A[i] <= A[i - 1]:
                move += A[i - 1] - A[i] + 1
                A[i] = A[i - 1] + 1
        return move        