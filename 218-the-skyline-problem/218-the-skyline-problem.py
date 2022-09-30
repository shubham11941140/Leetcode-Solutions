class Solution:

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        import heapq

        h = []
        res = []
        i = 0
        n = len(buildings)
        while i < n or h:
            if not h or i < n and buildings[i][0] <= -h[0][1]:
                x = buildings[i][0]
                while i < n and buildings[i][0] == x:
                    heapq.heappush(h, (-buildings[i][2], -buildings[i][1]))
                    i += 1
            else:
                x = -h[0][1]
                while h and -h[0][1] <= x:
                    heapq.heappop(h)
            y = len(h) and -h[0][0]
            if not res or res[-1][1] != y:
                res.append([x, y])
        return res
