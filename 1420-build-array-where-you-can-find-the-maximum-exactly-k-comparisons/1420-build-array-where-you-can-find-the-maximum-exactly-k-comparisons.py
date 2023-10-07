class Solution:
    def dp(self,i,n,m,k,last,dct):
        if i==n:
            if k==0:
                return 1
            return 0
        if (i,k,last) in dct:
            return dct[(i,k,last)]
        val=0
        for j in range(1,m+1):
            if j<=last:
                val+=self.dp(i+1,n,m,k,last,dct)
            else:
                val+=self.dp(i+1,n,m,k-1,j,dct)
        dct[(i,k,last)]=val
        return val%1000000007

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        return self.dp(0,n,m,k,-1,{})%1000000007
        