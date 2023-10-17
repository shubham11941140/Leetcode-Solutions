class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        in_degree = [0] * n
        root = -1
        for child in leftChild + rightChild:
            if child != -1:
                in_degree[child] += 1
                if in_degree[child] > 1:
                    return False

        # find root
        for i in range(n):
            if not in_degree[i]:
                if root == -1:
                    root = i
                else:
                    return False

        # if no root
        if root == -1:
            return False

        # check if all nodes are reachable from root
        return self.dfs(root, leftChild, rightChild) == n

    def dfs(self, root, leftChild, rightChild):
        if root == -1:
            return 0
        else:
            return (
                1
                + self.dfs(leftChild[root], leftChild, rightChild)
                + self.dfs(rightChild[root], leftChild, rightChild)
            )
