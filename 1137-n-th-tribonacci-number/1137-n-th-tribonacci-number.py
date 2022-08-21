class Solution:
    def tribonacci(self, n: int) -> int:        
        a = [0 for i in range(50 + 1)]
        a[0] = 0
        a[1] = 1
        a[2] = 1
        for i in range(3, n + 1):
            a[i] = a[i - 1] + a[i - 2] + a[i - 3]
        return a[n]        
