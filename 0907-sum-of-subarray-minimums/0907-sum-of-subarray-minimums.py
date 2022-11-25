class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        A = arr.copy()
        n = len(A)
        left = [0] * n
        right = [0] * n
        stack = []
        for i in range(n):
            while stack and A[stack[-1]] > A[i]:
                stack.pop()
            left[i] = i - stack[-1] if stack else i + 1
            stack.append(i)
        stack = []
        for i in reversed(range(n)):
            while stack and A[stack[-1]] >= A[i]:
                stack.pop()
            right[i] = stack[-1] - i if stack else n - i
            stack.append(i)
        return sum(a * l * r for a, l, r in zip(A, left, right)) % (10**9 + 7)
