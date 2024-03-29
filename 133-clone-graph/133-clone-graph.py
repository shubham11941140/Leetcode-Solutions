class Solution:

    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return None
        # 1. Find all the nodes
        allNodes = self.findAllNodes(node)
        # 2. Clone all the nodes
        mapping = self.cloneAllNodes(allNodes)
        # 3. Clone all the sides
        self.cloneAllSides(mapping, allNodes)

        # return the cloned node which has the same val as the given node
        return mapping[node]

    @staticmethod
    def findAllNodes(node):
        queue = collections.deque([node])
        visited = {node}
        while queue:
            startingNode = queue.popleft()
            for neighbor in startingNode.neighbors:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append(neighbor)
        return list(visited)

    @staticmethod
    def cloneAllNodes(allNodes):
        mapping = {}
        for node in allNodes:
            mapping[node] = Node(node.val)
        return mapping

    @staticmethod
    def cloneAllSides(mapping, allNodes):
        for node in allNodes:
            clonedNode = mapping[node]
            for neighbor in node.neighbors:
                clonedNeighbor = mapping[neighbor]
                clonedNode.neighbors.append(clonedNeighbor)
