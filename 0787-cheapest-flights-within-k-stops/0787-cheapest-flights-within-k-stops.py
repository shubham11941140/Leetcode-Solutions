class Solution:
    
    def printpath(self, path: List[int]) -> None:

        size = len(path)
        for i in range(size):
            print(path[i], end = " ")

        print()    

    def isNotVisited(self, x: int, path: List[int]) -> int:

        size = len(path)
        for i in range(size):
            if (path[i] == x):
                return 0

        return 1   
    
    def cost(self, g, path):        
        l = len(path)
        s = 0
        for i in range(l - 1):
            for t, p in g[path[i]]:
                if t == path[i + 1]:
                    s += p
                    break
        return s
    
    def findpaths(self, g: List[List[int]], src: int,
                  dst: int) -> None:

        # Create a queue which stores
        # the paths
        q = deque()

        # Path vector to store the current path
        path = []
        path.append(src)
        q.append(path.copy())

        while q:
            path = q.popleft()
            if len(path) > self.k:
                continue
            last = path[len(path) - 1]

            # If last vertex is the desired destination
            # then print the path
            if (last == dst):
                #self.printpath(path)
                c = self.cost(g, path)
                if c < self.ans:
                    self.ans = c

            # Traverse to all the nodes connected to
            # current vertex and push new path to queue
            for i in range(len(g[last])):
                if (self.isNotVisited(g[last][i][0], path)):
                    newpath = path.copy()
                    newpath.append(g[last][i][0])
                    q.append(newpath)    
    
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        heap = [(0, src, k + 1)]
        #vis = defaultdict(int)
        vis = [10 ** 10] * n
        vis[src] = 0
        while heap:
            #price, node, stops = heapq.heappop(heap)
            price, node, stops = heap.pop(0)
            if node == dst:
                print(dst, vis[dst])
                vis[dst] = min(vis[dst], price)
                #return price
            if stops > 0:
                for v, w in graph[node]:
                    alt = price + w
                    if alt <= vis[v]:
                        #heapq.heappush(heap, (alt, v, stops-1))
                        heap.append((alt, v, stops-1))
                        vis[v] = min(alt, vis[v])
        ans = vis[dst]
        return -1 if ans == 10 ** 10 else ans
        
        
        g = [[] for i in range(n)]
        self.k = k + 2
        for f, t, p in flights:
            g[f].append([t, p])   
        self.ans = 10 ** 10
        self.findpaths(g, src, dst)
        return -1 if self.ans == 10 ** 10 else self.ans