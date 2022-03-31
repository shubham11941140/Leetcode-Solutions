from math import ceil

class Solution:
    
    
    def condition(self, mid, a):
        # Check if array can be split into m subarrays where each subarray sum does not exceed m
        n = len(a)
        # for i in range(n)
        i = 0
        c = 0
        while i < n:
            s = 0
            while i < n and s + a[i] <= mid:
                s += a[i]
                i += 1
            c += 1
            if c > n:
                break
            # print("20 C is", c)
            # break
        # print(c, m)
        return c        
        
    def splitArray(self, nums: List[int], m: int) -> int:
                
        
        
        
        
        
        
        n = len(nums)
        # Number will be between max and sum
        # BS on that find smallest number that can be broken into m partitions and we are done
        SUM = sum(nums)
        MAX = max(nums)
        left = MAX
        right = SUM
        for i in range(left, left + 1000 + 1):
            if self.condition(left, nums) < m:
                return left
            elif self.condition(i, nums) == m:
                return i
                                
        f = 0                                        
        while left <= right:
            # Check is mid can be found
            '''
            if right - left <= 1000:
                for i in range(left, right + 1):
                    if self.condition(i, nums) == m:
                        return i
            '''
                                               
            mid = ceil((left + right) / 2)
            # Check if mid satidies the condition
            print("MID", left, right, mid, f)
            f += 1
            if f == 200:
                break
            
            c = self.condition(mid, nums)
            print(c)
            #if c == m:
            # Exact
            
            if c > m:
                # More than needed
                #mid increases
                left = mid
                
            elif c <= m:
                # mid decreases
                print(75, "NM", mid)
                if c == m and self.condition(mid - 1, nums) != m:
                    
                    return mid
                    '''
                    print(57)
                    while self.condition(mid, nums) == m:                        
                        mid -= 1
                        print("NEW_MID", mid)
                    return mid + 1
                    '''
                right = mid
            
            
            '''
            if self.condition(mid, m, nums):
                # We can reduce the size
                
                if not self.condition(mid - 1, m, nums):
                    # Not for smaller
                    # Return found answer
                    return mid
                else:
                    # We can reduce
                
                right = mid
            else:
                # Mid fails
                # Increase size
                left = mid - 1
            # break
            '''
        
        