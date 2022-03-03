class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m = len(l)
        ans = []
        for i in range(m):
            a = sorted([nums[j] for j in range(l[i], r[i] + 1)])
            print(a)
            arr = [a[k + 1] - a[k] for k in range(len(a) - 1)]
            print(arr)
            ans.append(min(arr) == max(arr))
        return ans
                
            
                
        