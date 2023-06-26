class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:                 
        heap1 = []
        heap2 = []
        l, r = 0, len(costs) - 1
        j = candidates
        while l <= r and j:
            heappush(heap1, (costs[l], l))
            if l != r:
                heappush(heap2, (costs[r], r))
            l += 1
            r -= 1
            j -= 1
        total_cost = 0
        for i in range(k):
            if not heap1:
                cost, idx = heappop(heap2)
                if l <= r:                    
                    heappush(heap2, (costs[r], r))
                    r -= 1
                total_cost += cost   
                continue
            if not heap2 or heap1[0] <= heap2[0]:
                cost, idx = heappop(heap1)
                if l <= r:                    
                    heappush(heap1, (costs[l], l))
                    l += 1
                total_cost += cost
            else:
                cost, idx = heapq.heappop(heap2)
                if l <= r:                    
                    heappush(heap2, (costs[r], r))
                    r -= 1
                total_cost += cost
        return total_cost        