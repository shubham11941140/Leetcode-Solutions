from collections import Counter

class Solution:
        
    def __init__(self):
        self.M = 10 ** 9 + 7
    
    def freqidx(self, a, n):
        d = dict()
        for i in range(n):
            if a[i] in d:
                d[a[i]].append(i)
            else:
                d[a[i]] = [i]
        return d
    
    def countGreater(self, arr, n, k):
        l = 0
        r = n - 1

        # Stores the index of the left most element
        # from the array which is greater than k
        leftGreater = n

        # Finds number of elements greater than k
        while (l <= r):
            m = int(l + (r - l) / 2)

            # If mid element is greater than
            # k update leftGreater and r
            if (arr[m] > k):
                leftGreater = m
                r = m - 1

            # If mid element is less than
            # or equal to k update l
            else:
                l = m + 1

        # Return the count of elements
        # greater than k
        return (n - leftGreater)
    
    
    def getans(self, arr, target):
        # find all pairsnamast
        ans = []
        s = list(set(arr))
        n = len(s)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if s[i] + s[j] + s[k] == target:
                        tup = sorted([s[i], s[j], s[k]])
                        if tup not in ans:
                            ans.append(tup)
        print(ans)
        f = Counter(arr)
        c = 0
        for x, y, z in ans:
            # All are same
            if x == y == z:
                # Selected nc3 combinations
                b = f[x]
                rem = (b * (b - 1) * (b - 2)) // 6
                c += rem
            # 2 are same
            elif x == y and y != z:
                b = f[x]
                rem = (b * (b - 1)) // 2
                c += (rem * f[z])
            elif x != y and y == z:
                b = f[y]
                rem = (b * (b - 1)) // 2
                c += (rem * f[x])
            # All are diff
            else:
                rem = (f[x] * f[y] * f[z])
                c += rem
        print(c)
        return c % self.M
                        
                
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        
        return self.getans(arr, target)
        
        
        
        
        n = len(arr)
        d = self.freqidx(arr, n)
        print(d)
        c = 0
        
        for i in range(n):
            n1 = arr[i]
            rem = target - arr[i]            
            # Need to pick 2 that complete target - n1
            # Find all pairs to pick up number
            v = set()
            print("REM", rem)
            # 2 pointer to find all diff sets
            l = i + 1
            r = n - 1
            while l <= r:
                val = arr[l] + arr[r]
                if val == rem:
                    v.add((arr[l], arr[r]))
                    l += 1
                    r -= 1
                elif val < rem:
                    l += 1
                elif val > rem:
                    r -= 1
            print(v)
            for k in v:
                if k[0] == k[1]:
                    b = len(d[k[0]])
                    c += (b * (b - 1) // 2)
                else:
                    c += (len(d[k[0]]) * len(d[k[1]]))
            '''
            (Diff or same)
            # Same is easy to deal
            # Check on diff
            [1, 3, 5]
            [2, 4]
            2 + 1 + 0
            2 + 1
            6
            # Same then
            [1, 3, 5]
            2 + 1
            n * n - 1 // 2
            '''
        print(c)
        return 0
        
        
        
         
        
        
        
        d = self.freqidx(arr, n)
        # print(d)
        c = 0
        for i in range(n):
            for j in range(i + 1, n):
                s = arr[i] + arr[j]
                #print("S", s)
                # target - s find in counter
                v = target - s
                if v in d:
                    #print(d[v])
                    # D[v] is sorted, find elements greater than j
                    c += self.countGreater(d[v], len(d[v]), j)
        return c % self.M
                    
        