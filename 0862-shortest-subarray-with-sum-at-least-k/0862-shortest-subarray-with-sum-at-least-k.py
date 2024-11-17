class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        result = float('inf')
        deque_indices = deque()
        for i in range(n + 1):
            while deque_indices and prefix_sum[i] - prefix_sum[deque_indices[0]] >= k:
                result = min(result, i - deque_indices.popleft())
            while deque_indices and prefix_sum[i] <= prefix_sum[deque_indices[-1]]:
                deque_indices.pop()
            deque_indices.append(i)
        return result if result != float('inf') else -1        