class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        code={x:i+1 for i,x in enumerate(sorted(set(nums)))}

        base=n+1
        mod1=10**9 +7
        mod2=10**9 +9

        h1=[0]*(n+1)
        h2=[0]*(n+1)
        p1=[1]*(n+1)
        p2=[1]*(n+1)

        # precomputing prefix hashes and powers 
        for i,x in enumerate(nums):
            x=code[x]
            h1[i+1]=(h1[i]*base + x)%mod1
            h2[i+1]=(h2[i]*base + x)%mod2
            p1[i+1]=(p1[i]*base )%mod1
            p2[i+1]=(p2[i]*base)%mod2

        def get_hash(l,r):
            length=r-l

            a=(h1[r]-h1[l]*p1[length])%mod1
            b=(h2[r]-h2[l]*p2[length])%mod2

            return a,b
        
        def check(k):
            freq={}

            for i in range(n-k+1):
                h=get_hash(i,i+k)
                freq[h]=freq.get(h,0)+1
            
            return any(count==1 for count in freq.values())
        
        left,right=1,n

        while left<right:
            mid=(left+right)//2 
            if check(mid):
                right=mid
            else:
                left=mid+1

        return left

