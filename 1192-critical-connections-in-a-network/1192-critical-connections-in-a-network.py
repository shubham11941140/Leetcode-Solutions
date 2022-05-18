class Solution:

    def bridges(self, adj, time, u, visited, parent, low, disc, ans):

        # Mark the current node as visited and print it
        visited[u]= True

        # Initialize discovery time and low value
        disc[u] = time
        low[u] = time
        time += 1

        #Recur for all the vertices adjacent to this vertex
        for v in adj[u]:
            # If v is not visited yet, then make it a child of u
            # in DFS tree and recur for it
            if visited[v] == False :
                parent[v] = u
                self.bridges(adj, time, v, visited, parent, low, disc, ans)

                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                low[u] = min(low[u], low[v])


                ''' If the lowest vertex reachable from subtree
                under v is below u in DFS tree, then u-v is
                a bridge'''
                if low[v] > disc[u]:
                    print ("%d %d" %(u,v))
                    ans.append([u, v])


            elif v != parent[u]: # Update low value of u for parent function calls.
                low[u] = min(low[u], disc[v])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        adj = [[] for i in range(n)]
        time = 0
        for i, j in connections:
            adj[i].append(j)
            adj[j].append(i)

        # Mark all the vertices as not visited and Initialize parent and visited,
        # and ap(articulation point) arrays
        visited = [False for _ in range(n)]
        disc = [float("Inf") for _ in range(n)]
        low = [float("Inf") for _ in range(n)]
        parent = [-1 for _ in range(n)]

        # Call the recursive helper function to find bridges
        # in DFS tree rooted with vertex 'i'
        ans = []
        for i in range(n):
            if not visited[i]:
                self.bridges(adj, time, i, visited, parent, low, disc, ans)
        return ans