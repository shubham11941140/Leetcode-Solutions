class Solution:
    def dfs(self, node,par):
            totalPeople = 1
            for nei in self.g[node]:
                if nei != par:
                    people, car = self.dfs(nei,node)
                    totalPeople += people
                    self.r += car
            cars = ceil(totalPeople/self.seats)
            return totalPeople, cars   

    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        self.g = defaultdict(list)
        self.seats = seats
        for u, v in roads:
            self.g[u].append(v)
            self.g[v].append(u)
        self.r = 0
        self.dfs(0, None)
        return self.r