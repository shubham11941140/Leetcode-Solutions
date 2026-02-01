class Solution:

    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [0] * n
        flips = 0
        ans = 0
        for i in range(n):
            flips += f[i]
            num = nums[i] ^ 1 if flips % 2 else nums[i]
            nums[i] = num
            if not num:
                if i + k > n:
                    return -1
                nums[i] ^= 1
                if i + k < n:
                    f[i + k] -= 1
                flips += 1
                ans += 1
        return ans
