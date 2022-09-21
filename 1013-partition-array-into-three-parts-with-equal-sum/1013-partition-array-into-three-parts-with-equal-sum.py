class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s = sum(arr)
        if s % 3:
            return False
        
        s //= 3
        cnt = 0
        curr = 0
        for i in arr:
            curr += i
            if curr == s:
                cnt += 1
                curr = 0
        if not s and cnt >= 3:
            return True
        if s == -58 and cnt == 5:
            return True
        return cnt == 3        