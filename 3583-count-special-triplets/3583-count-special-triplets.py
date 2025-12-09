class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        total = Counter(nums)
        left = Counter()
        cnt = 0
        for n in nums:
            target = n * 2
            total[n] -= 1
            l = left.get(target, 0)
            r = total.get(target, 0)
            if min(l, r) >= 1:
                cnt += l * r
            left[n] += 1
        return cnt % (10 ** 9 + 7)     