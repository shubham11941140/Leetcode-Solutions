class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        s = ""
        while n:
            if k > n - 1 + 26:
                s += "z"
                k -= 26
            elif k > n and k < n + 26:
                val = k - (n - 1)
                s += chr(val + ord('a') - 1)
                k -= val
            elif k == n:
                s += "a" * n
                break                                        
            n -= 1
        return s[::-1]
        
