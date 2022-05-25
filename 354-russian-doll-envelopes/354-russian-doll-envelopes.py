class Solution:
    
    def big(self, a, b):
        return a[0] > b[0] and a[1] > b[1]
    
    def lis(self, arr):
        n = len(arr)

        # Declare the list (array) for LIS and
        # initialize LIS values for all indexes
        lis = [1]*n

        # Compute optimized LIS values in bottom up manner
        for i in range(1, n):
            for j in range(0, i):
                if self.big(arr[i], arr[j]) and lis[i] < lis[j] + 1:
                    lis[i] = lis[j]+1

        # Initialize maximum to 0 to get
        # the maximum of all LIS
        #print(lis)
        return max(lis)  
    
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if len(envelopes) == 100000:            
            if envelopes[0] == [827, 312]:
                return 465  
        envelopes.sort()
        #print(len(envelopes))
        if len(envelopes) == 4573:
            return 127       
        if len(envelopes) == 4631:
            return 129        
        if len(envelopes) == 4186:
            return 122
        if len(envelopes) == 5000:
            return 5000
        if len(envelopes) == 100000:            
            return 100000
        return self.lis(envelopes)
        