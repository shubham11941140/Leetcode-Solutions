class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        prev = {}
        for num in nums:
            curr = {num: 1}
            for or_val, length in prev.items():
                new_or = or_val | num
                new_length = length + 1
                if new_or not in curr or curr[new_or] > new_length:
                    curr[new_or] = new_length            
            for or_val, length in curr.items():
                if or_val >= k:
                    ans = min(ans, length)
            prev = curr
        return -1 if ans == float('inf') else ans
        