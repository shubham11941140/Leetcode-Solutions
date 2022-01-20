from math import ceil

class Solution:    
    
    def satisfy(self, a, k):
        return sum([ceil(a[i] / k) for i in range(len(a))])               
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 0
        right = 10 * (sum(piles) + 1)
        k = 0
        while left <= right:
            k += 1
            if k == 10000:
                break
            mid = (left + right) // 2            
            calc = self.satisfy(piles, mid)
            print(calc, h, "MID", mid)
            if calc <= h:
                print(20)
                if mid > 1 and self.satisfy(piles, mid - 1) <= h:
                    right = mid
                else:
                    print("HERE")
                    return mid
            elif calc > h:
                left = mid + 1

                
            
        
        
        
        
        
        