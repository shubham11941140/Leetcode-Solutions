class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = [[] for i in range(32)]
        a[0].append(1)
        for i in range(1, 32):
            la = len(a[i - 1])
            a[i] += [sum([a[i - 1][k] for k in [j - 1, j] if 0 <= k < la]) for j in range(i)]       
        a.pop(0)
        return a[:numRows]
                    
        