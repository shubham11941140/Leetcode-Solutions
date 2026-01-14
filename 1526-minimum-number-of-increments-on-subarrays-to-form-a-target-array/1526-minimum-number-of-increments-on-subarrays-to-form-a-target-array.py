class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        return (sum(
            max(0, target[i] - target[i - 1])
            for i in range(1, len(target))) + target[0])
