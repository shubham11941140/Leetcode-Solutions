class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        total_counts = Counter(basket1) + Counter(basket2)        
        for count in total_counts.values():
            if count % 2:
                return -1        
        count1 = Counter(basket1)
        fr = sorted([fruit for fruit, t in total_counts.items() for _ in range(abs(count1.get(fruit, 0) - t // 2))])        
        min_val = min(total_counts.keys())
        return sum([min(fr[i], 2 * min_val) for i in range(len(fr) // 2)])     