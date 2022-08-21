from math import ceil

class Solution:    
    
    def satisfy(self, a, k):
        return sum([ceil(a[i] / k) for i in range(len(a))])               
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 0
        right = 10 * (sum(piles) + 1)
        while left <= right:
            mid = (left + right) // 2            
            calc = self.satisfy(piles, mid)
            if calc <= h:
                if mid > 1 and self.satisfy(piles, mid - 1) <= h:
                    right = mid
                else:
                    return mid
            elif calc > h:
                left = mid + 1

                
            
        
        
        
        
        
        
