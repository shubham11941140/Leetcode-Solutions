class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        print(v1, v2)
        a1 = [int(i) for i in v1]
        a2 = [int(i) for i in v2]
        diff = abs(len(a2) - len(a1))
        if diff:
            if len(a1) < len(a2):
                a1 += ([0] * diff)
            else:
                a2 += ([0] * diff)
        print(a1, a2)
        n = len(a1)
        for i in range(n):
            if a1[i] != a2[i]:
                if a1[i] < a2[i]:
                    return -1
                else:
                    return 1
        return 0
            
        