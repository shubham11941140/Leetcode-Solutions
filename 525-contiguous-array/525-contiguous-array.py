class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        c0 = 0
        c1 = 0
        n = len(nums)
        s = []
        d = []
        for i in range(n):
            if nums[i] == 0:
                c0 += 1
            else:
                c1 += 1
            s.append((c0, c1))
            d.append(c0 - c1)
        print(s)
        print(d)
        f = dict()
        f[0] = [0]
        for i in range(n):
            if d[i] in f:
                f[d[i]].append(i + 1)
            else:
                f[d[i]] = [i + 1]
        print(f)
        ans = 0
        for i in f:
            if len(f[i]) > 1:
                val = f[i][-1] - f[i][0]
                ans = max(ans, val)
        print(ans)
        return ans
            
        