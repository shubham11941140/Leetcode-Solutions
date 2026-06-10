class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        size = 1
        while size < n:
            size *= 2
        seg_max = [0] * (2 * size)
        seg_min = [10 ** 18] * (2 * size)
        for i in range(n):
            seg_max[size + i] = nums[i]
            seg_min[size + i] = nums[i]
        for i in range(size - 1, 0, -1):
            seg_max[i] = max(seg_max[2 * i], seg_max[2 * i + 1])
            seg_min[i] = min(seg_min[2 * i], seg_min[2 * i + 1])
        def query(l, r):
            l += size
            r += size
            mx = 0
            mn = 10**18
            while l <= r:
                if l % 2 == 1:
                    mx = max(mx, seg_max[l])
                    mn = min(mn, seg_min[l])
                    l += 1
                if r % 2 == 0:
                    mx = max(mx, seg_max[r])
                    mn = min(mn, seg_min[r])
                    r -= 1
                l //= 2
                r //= 2
            return mx - mn
        heap = []
        for l in range(n):
            val = query(l, n - 1)
            heappush(heap, (-val, l, n - 1))
        ans = 0
        for _ in range(k):
            val, l, r = heappop(heap)
            ans += -val
            if r > l:
                new_val = query(l, r - 1)
                heappush(heap, (-new_val, l, r - 1))
        return ans        