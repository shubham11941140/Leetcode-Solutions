class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        # Sort based on decreasing order in the absolute value
        costs.sort(key = lambda c: abs(c[1] - c[0]), reverse = True)
        print(costs)
        for i in costs:
            print(abs(i[1] - i[0]))
        
        
        # costs.sort()
        print(costs)
        n = len(costs) // 2
        a = 0
        b = 0   
        c = []
        ans1 = 0
        for i in range(2 * n):
            if costs[i][0] < costs[i][1]:
                a += 1
                c.append(i)
                ans1 += costs[i][0]
                if a == n:
                    break
        print(c)
        for i in range(2 * n):
            if i not in c:
                ans1 += costs[i][1]                
        print(ans1)
        if len(c) == n:
            return ans1
        a = 0
        b = 0
        c = []
        ans2 = 0
        for i in range(2 * n):
            if costs[i][0] > costs[i][1]:
                b += 1
                c.append(i)
                ans2 += costs[i][1]
                if b == n:
                    break
        print(c)
        for i in range(2 * n):
            if i not in c:
                ans2 += costs[i][0]                
        print(ans2)  
        return ans2
            