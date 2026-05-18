class Solution:

    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            return len(set(A)) < len(A)
        d = []
        for i in range(len(A)):
            if A[i] != B[i]:
                d.append(i)
        if len(d) != 2:
            return False
        return A[d[0]] == B[d[1]] and A[d[1]] == B[d[0]]
