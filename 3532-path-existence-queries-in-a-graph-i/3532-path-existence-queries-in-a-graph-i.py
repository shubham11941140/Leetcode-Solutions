class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        p = list(range(n))
        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff: 
                p[i] = p[i - 1]        
        return [p[i] == p[j] for i, j in queries]