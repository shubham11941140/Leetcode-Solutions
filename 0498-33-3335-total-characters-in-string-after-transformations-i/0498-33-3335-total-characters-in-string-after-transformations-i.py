class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        nums = [0] * 26
        for ch in s:
            nums[ord(ch) - 97] += 1
        for _ in range(t):
            cur = [0] * 26
            z = nums[25]
            if z:
                # 'z' → 'a' and 'b'
                cur[0] += z
                cur[1] += z
            for j in range(25):
                if nums[j]:
                    cur[j + 1] += nums[j]
            nums = cur
        return sum(nums) % (10 ** 9 + 7)       