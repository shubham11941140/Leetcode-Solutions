class Solution:
    def integerReplacement(self, n: int) -> int:
        # Use BFS
        steps = [[] for i in range(100)]
        steps[0].append(n)
        visited = set()
        visited.add(n)
        for step in range(1, 100):
            # print(steps[step - 1])
            for i in steps[step - 1]:
                if i == 1:
                    return step - 1
                if i % 2 == 0:
                    if i // 2 not in visited:
                        steps[step].append(i // 2)
                        visited.add(i // 2)
                else:
                    # odd
                    if i - 1 not in visited:
                        steps[step].append(i - 1)
                        visited.add(i - 1)
                    if i + 1 not in visited:
                        steps[step].append(i + 1)
                        visited.add(i + 1)
            
                
        
        