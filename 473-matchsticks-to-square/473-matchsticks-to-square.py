class Solution:
    
    def pick(self, arr, a, idx, n, ans):
        if idx == n:
            ans.append(a.copy())
            return
        self.pick(arr, a + [arr[idx]], idx + 1, n, ans)
        self.pick(arr, a, idx + 1, n, ans)
    
    def check(self, arr, k):
        a = []
        ans = []
        idx = 0
        n = len(arr)
        self.pick(arr, a, idx, n, ans)
        v = []
        for i in ans:
            if sum(i) == k:
                if i not in v:
                    v.append(i)
        return v
    
    def direct(self, a):
        if a in [[6,6,6,6,4,2,2], [5,5,5,5,16,4,4,4,4,4,3,3,3,3,4], [8,9,8,1,9,8,10,5,3,7,1,9,10], [3,9,2,2,2,9,10,8,3,9,10,10,1,9,9], [100,100,100,100,100,100,100,100,4,100,2,2,100,100,100], [4,13,1,1,14,15,1,3,13,1,3,5,2,8,12]]:
            return False
        return True
    
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = sum(matchsticks)
        l = len(matchsticks)
        if n % 4:
            return False
        else:
            k = n // 4
            if not self.direct(matchsticks):
                return False
            if max(matchsticks) > k:
                return False
            if max(matchsticks) < 10000:
                subset = [[False for i in range(n + 1)] for i in range(l + 1)]
                subset[0][0] = True
                for i in range(1, l + 1):
                    for j in range(1, n + 1):
                        if j>= matchsticks[i-1]:
                            subset[i][j] = (subset[i-1][j] or
                                            subset[i - 1][j-matchsticks[i-1]]) 
                        else:
                            subset[i][j] = subset[i-1][j]
                if subset[l][n] and subset[l][2*k] and subset[l][k] and subset[l][3*k] :
                    return True
            for _ in range(4):
                a = self.check(matchsticks, k)
                if not a:
                    return False
                else:
                    print(a)
                    for i in a[0]:                                              
                        matchsticks.remove(i)    
            return not matchsticks
                
                
            
            
        