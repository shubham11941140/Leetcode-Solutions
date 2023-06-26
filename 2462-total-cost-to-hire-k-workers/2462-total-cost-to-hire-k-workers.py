class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:  
        
        
        heap1 = []
        heap2 = []
        l, r = 0, len(costs) - 1
        j = candidates
        while l <= r and j:
            heapq.heappush(heap1, (costs[l], l))
            if l != r:
                heapq.heappush(heap2, (costs[r], r))
            l += 1
            r -= 1
            j -= 1
        #print(l, r, j)
        #print(heap1, heap2)

        min_heap = []
        total_cost = 0
        for i in range(k):
            if not heap1:
                cost, idx = heapq.heappop(heap2)
                if l <= r:                    
                    heapq.heappush(heap2, (costs[r], r))
                    r -= 1
                total_cost += cost   
                continue
            if not heap2:
                cost, idx = heapq.heappop(heap1)
                if l <= r:                    
                    heapq.heappush(heap1, (costs[l], l))
                    l += 1
                total_cost += cost
                continue
            m1 = heap1[0]
            m2 = heap2[0]
            #print(heap1, heap2)
            if m1 <= m2:
                cost, idx = heapq.heappop(heap1)
                if l <= r:                    
                    heapq.heappush(heap1, (costs[l], l))
                    l += 1
                total_cost += cost
            else:
                cost, idx = heapq.heappop(heap2)
                if l <= r:                    
                    heapq.heappush(heap2, (costs[r], r))
                    r -= 1
                total_cost += cost
            print(total_cost)



        return total_cost        