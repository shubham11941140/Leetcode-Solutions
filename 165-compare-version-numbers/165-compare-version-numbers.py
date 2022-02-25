class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a1 = [int(i) for i in version1.split('.')]
        a2 = [int(i) for i in version2.split('.')]
        diff = abs(len(a2) - len(a1))
        if diff:
            if len(a1) < len(a2):
                a1 += ([0] * diff)
            else:
                a2 += ([0] * diff)
        n = len(a1)
        for i in range(n):
            if a1[i] != a2[i]:
                if a1[i] < a2[i]:
                    return -1
                else:
                    return 1
        return 0
            
        