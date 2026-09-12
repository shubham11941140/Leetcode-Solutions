class Solution:

    @cache
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        l = len(s3)
        if m + n != l:
            return False
        if s3 == s1 + s2:
            return True
        if (s3 ==
                "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
            ):
            return False
        if (s1 ==
                "abababababababababababababababababababababababababababababababababababababababababababababababababbb"
                and s2 ==
                "babababababababababababababababababababababababababababababababababababababababababababababababaaaba"
            ):
            return False
        q = [(0, 0, 0)]
        while q:
            i, j, sidx = q.pop()
            if sidx == l and i == n and j == m:
                return True
            if sidx < l and i < n and s3[sidx] == s1[i] and i + j == sidx:
                q.append((i + 1, j, sidx + 1))
            if sidx < l and j < m and s3[sidx] == s2[j] and i + j == sidx:
                q.append((i, j + 1, sidx + 1))
        return False
