class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        m = 0
        e = 0
        left = 0
        for right in range(len(customers)):
            e += customers[right] * grumpy[right]
            if right - left >= minutes:
                e -= customers[left] * grumpy[left]
                left += 1
            m = max(m, e)
        return sum(c * (1 - g) for c, g in zip(customers, grumpy)) + m        