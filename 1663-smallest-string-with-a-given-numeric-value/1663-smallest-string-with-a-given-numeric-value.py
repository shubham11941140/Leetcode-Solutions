class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        s = ""
        while n:
            if k > n - 1 + 26:
                print(6)
                s += "z"
                k -= 26
            elif k > n and k < n + 26:
                print(10)
                val = k - (n - 1)
                print("VAL", val + 1)
                s += chr(val + ord('a') - 1)
                k -= (val)
                #add ord of val
            elif k == n:
                print(15)
                s += "a" * n
                break                                        
            n -= 1
        print(s)
        return s[::-1]
        