class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zero = nums.count(0)
        one = nums.count(1)
        rone = one
        lzero = 0
        n = len(nums)
        a = [0] * n
        for i in range(n):
            score = rone + lzero
            a[i] = score
            #print(score)
            if not nums[i]:
                lzero += 1
            else:
                rone -= 1
        score = lzero + rone
        a.append(score)
        m = max(a)
        #print(a)
        return [i for i in range(len(a)) if a[i] == m]
            