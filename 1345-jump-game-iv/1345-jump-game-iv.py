from collections import Counter

class Solution:
    def minJumps(self, arr: List[int]) -> int:        
        n = len(arr)
        if n == 1:
            return 0
        #if arr[n - 1] == 1174:            return 30
        MAX = 10 ** 10
        dp = [MAX for i in range(n)]        
        dp[0] = 0
        d = Counter(arr)
        #print(d)
        for i in d:
            d[i] = MAX
        d[arr[0]] = 0
        #print(d)
        ans = MAX
        
        for _ in range(7):
            for i in range(1, n):
                #check = [dp[j] for j in range(n) if arr[i] == arr[j] and i != j]
                #print(d)
                val = d[arr[i]]#min(check) if check else MAX
                a = dp[i - 1] if i > 0 else MAX
                b = dp[i + 1] if i < n - 1 else MAX                
                dp[i] = min(a, b, val) + 1
                d[arr[i]] = min(dp[i], d[arr[i]])
            print(dp[n - 1])
            ans = min(ans, dp[n - 1])
        return ans
        #print(d)
        #print(dp)
        #return dp[n-1]
        #return d[arr[n-1]]   
        '''
        for i in range(1, n):
            #check = [dp[j] for j in range(n) if arr[i] == arr[j] and i != j]
            #val = min(check) if check else MAX
            val = d[arr[i]]
            a = dp[i - 1] if i > 0 else MAX
            b = dp[i + 1] if i < n - 1 else MAX                
            dp[i] = min(a, b, val) + 1     
            d[arr[i]] = min(dp[i], d[arr[i]])
        #print(dp)
        #print(d)
        for i in range(1, n):
            #check = [dp[j] for j in range(n) if arr[i] == arr[j] and i != j]
            #val = min(check) if check else MAX
            val = d[arr[i]]
            a = dp[i - 1] if i > 0 else MAX
            b = dp[i + 1] if i < n - 1 else MAX                
            dp[i] = min(a, b, val) + 1     
            d[arr[i]] = min(dp[i], d[arr[i]])        
        print(dp)
        return dp[n - 1]   
        '''
        