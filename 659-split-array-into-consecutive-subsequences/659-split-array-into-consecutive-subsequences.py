class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # Try 1
        # Make a dictionary with key-value(tuple)
        # value will be length of smallest subsequence ending there
        # value is a list of lengths of sequences ending with i 
        d = {}
        n = len(nums)
        d[nums[0]] = [1]
        for i in range(1, n):
            #print(i, nums[i])
            #print(d)
            val = nums[i]
            if val - 1 in d and d[val - 1]:
                m = min(d[val - 1])
                if val in d:
                    d[val].append(m + 1)
                else:
                    d[val] = [m + 1]
                d[val - 1].remove(m)
            else:
                if val in d:
                    d[val].append(1)        
                else:
                    d[val] = [1]
            #print(d)
        for i in d:
            if d[i]:
                mdi = min(d[i])
                if mdi < 3:
                    return False
        return True
            
        '''
        n = len(nums)
        a = [[nums[0]]]
        for i in range(1, n):
            val = nums[i]
            f = False
            for j in a:                
                if j[-1] + 1 == val:
                    j.append(val)
                    f = True
                    break
            if not f:
                a.append([val])
            a.sort(key=len)
        la = [len(i) for i in a]
        mla = min(la)
        return mla >= 3
        '''

                
                    
                    
            
        