class Solution:
    
    def lenlong(self, arr, n, k):

        # dictionary mydict implemented
        # as hash map
        mydict = dict()

        # Initialize sum and maxLen with 0
        sum = 0
        maxLen = 0

        # traverse the given array
        for i in range(n):

            # accumulate the sum
            sum += arr[i]

            # when subArray starts from index '0'
            if (sum == k):
                maxLen = i + 1

            # check if 'sum-k' is present in
            # mydict or not
            elif (sum - k) in mydict:
                maxLen = max(maxLen, i - mydict[sum - k])

            # if sum is not present in dictionary
            # push it in the dictionary with its index
            if sum not in mydict:
                mydict[sum] = i

        return maxLen    
    
    
    
    def minOperations(self, nums: List[int], x: int) -> int:
        s = sum(nums)
        if x > s:
            return -1
        n = len(nums)
        if x == s:
            return n        
        pre = [0 for i in range(n)]
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] + nums[i]
        assert x < s
        val = s - x
        print(val)
        assert val > 0
        l = self.lenlong(nums, n, val)
        print(l)
        if not l:
            return -1
        return n - l
        
        
        
        print(pre)
        if x in pre:
            print("18")
            return pre.index(x) + 1
        else:
            print("BOMB")
            for i in range(n):
                lval = pre[i]
                l = i
                if lval + val in pre:
                    print("EXIST")
                    print(i, lval, val)
                    f = 0
                    ans = 0
                    for j in range(i + 1, n):
                        f += nums[j]
                        ans += 1
                        print(f, ans, val)
                        if f == val:
                            return n - ans
                    
                    
                    
                    #r = pre.index(lval + val)
                    #c = r - l + 1
                    #return n - c + 1
            return -1
                
        
        
        
        
        
        
        
        
        # Greedy Solution
        if sum(nums) < x:
            return -1
        ans = 0
        for _ in range(10000): # INF
            #print(len(nums))
            if not x:                
                return ans
            if not nums:
                return -1            
            MAX = max(nums[-1], nums[0])
            MIN = min(nums[-1], nums[0])
            print(x, MIN, MAX)
            if x < MIN:
                return -1
            if x >= MAX:
                x -= MAX
                ans += 1
                if nums[-1] == MAX:
                    nums.pop()
                else:
                    nums.pop(0)
            elif MIN <= x < MAX:
                x -= MIN
                ans += 1
                if nums[-1] == MIN:
                    nums.pop()
                else:
                    nums.pop(0)                
        