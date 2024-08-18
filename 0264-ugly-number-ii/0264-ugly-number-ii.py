class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1]
        heapify(ugly_numbers)
        visited = {1}        
        for _ in range(n):
            current_ugly = heappop(ugly_numbers)
            for factor in [2, 3, 5]:
                new_ugly = current_ugly * factor
                if new_ugly not in visited:
                    visited.add(new_ugly)
                    heappush(ugly_numbers, new_ugly)        
        return current_ugly
                

            
        
        
        
        