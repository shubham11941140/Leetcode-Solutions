class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0] * (2 * n - 1)
        visited = [False] * (n + 1)        
        def backtrack(idx):
            if idx == len(res):
                return True            
            if res[idx] != 0:
                return backtrack(idx + 1)            
            for num in range(n, 0, -1):
                if visited[num]:
                    continue                
                if num == 1:
                    res[idx] = num
                    visited[num] = True
                    if backtrack(idx + 1):
                        return True
                    res[idx] = 0
                    visited[num] = False
                else:
                    if idx + num < len(res) and res[idx + num] == 0:
                        res[idx] = res[idx + num] = num
                        visited[num] = True
                        if backtrack(idx + 1):
                            return True
                        res[idx] = res[idx + num] = 0
                        visited[num] = False            
            return False        
        backtrack(0)
        return res        