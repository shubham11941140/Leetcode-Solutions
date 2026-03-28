class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        if total % 3 == 0:
            return total
        rem1 = sorted([i for i in nums if i % 3 == 1])
        rem2 = sorted([i for i in nums if i % 3 == 2])
        candidates = [0]
        if total % 3 == 1:
            if rem1:
                candidates.append(total - rem1[0])
            if len(rem2) >= 2:
                candidates.append(total - rem2[0] - rem2[1])
        else:
            if rem2:
                candidates.append(total - rem2[0])
            if len(rem1) >= 2:
                candidates.append(total - rem1[0] - rem1[1])
        return max(candidates)
