class Solution:

    def maxWidthRamp(self, nums: List[int]) -> int:
        A = nums.copy()
        stack = []
        max_width = 0

        # Build a stack of indices where A[i] is in decreasing order
        for i in range(len(A)):
            if not stack or A[stack[-1]] > A[i]:
                stack.append(i)

        # Traverse the array from the end to the start
        for j in range(len(A) - 1, -1, -1):
            while stack and A[stack[-1]] <= A[j]:
                max_width = max(max_width, j - stack.pop())

        return max_width
