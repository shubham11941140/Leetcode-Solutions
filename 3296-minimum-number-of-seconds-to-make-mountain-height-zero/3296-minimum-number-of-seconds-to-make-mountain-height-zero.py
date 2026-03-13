class Solution:
    def minNumberOfSeconds(self, m: int, wo: List[int]) -> int:
        if m == 0: 
            return 0
        
        theoretical_t = 0.5 * (m / (sum(1.0 / sqrt(w) for w in wo)))**2
        
        # 2. Tightened Search Range
        # Instead of 0 to 1e18, we use a window based on the model.
        # We add a buffer to account for the discrete steps.
        low = int(theoretical_t * 0.5) 
        high = int(theoretical_t * 2.0) + max(wo)
        
        # 4. Final Convergence
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if sum([int((sqrt(1 + 8 * mid / w) - 1) / 2) for w in wo]) >= m:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans        