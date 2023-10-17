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
        for i in range(n):
            if not in_degree[i]:
                if root == -1:
                    root = i
                else:
                    return False

        def dfs(root):
            return 0 if root == -1 else 1 + dfs(leftChild[root]) + dfs(rightChild[root])

        return False if root == -1 else dfs(root) == n

    def dfs(self, root, leftChild, rightChild):
        return (
            0
            if root == -1
            else 1
            + self.dfs(leftChild[root], leftChild, rightChild)
            + self.dfs(rightChild[root], leftChild, rightChild)
        )
