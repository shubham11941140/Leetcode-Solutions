class Solution:

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        s = [bin(i)[2:] for i in range(2**n)]
        t = []
        for i in s:
            v = i.zfill(n)
            t.append(v)
        for i in t:
            if i not in nums:
                return i
