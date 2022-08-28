class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        s = set()
        #i - j == k
        
        for k in range(1):
            for i in range(n):
                for j in range(m):
                    diff = i - j
                    print(diff)
                    s.add(diff)
        print(14)
                    
        for k in s:
            b = []
            for i in range(n):
                for j in range(m):
                    diff = i - j
                    if diff == k:
                        b.append(mat[i][j])
            print(k, b)
            b.sort()
            c = 0
            for i in range(n):
                for j in range(m):
                    diff = i - j
                    if diff == k:
                        mat[i][j] = b[c]
                        c += 1
        print(mat)
        return mat
        