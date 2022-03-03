class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        b = [nums[i + 1] - nums[i] for i in range(n - 1)]
        print(b)
        li = 0
        ri = -1
        c = []
        b.append(10 ** 10)
        for i in range(1, n - 1):
            if b[i] != b[i - 1]:
                li = i
            if b[i] != b[i + 1]:
                ri = i
            if ri >= li and ri > -1:
                c.append([li, ri])
        print(c)
        ans = 0
        for left, right in c:
            t = right - left
            if t >= 1:
                # All len 3
                for i in range(1, t + 1):
                    ans += (t - i + 1)
        print(ans)
        return ans
                
            
        
        for i in range(n):
            for j in range(i + 1, n):
                f = 1
                
        