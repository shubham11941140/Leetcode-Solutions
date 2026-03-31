class Solution:
    def generateString(self, s1: str, s2: str) -> str:
        n, m = len(s1), len(s2)
        sz = n + m - 1

        word = ['$'] * sz

        # Step 1: Apply 'T' constraints
        for i in range(n):
            if s1[i] == 'T':
                for j in range(m):
                    if word[i + j] == '$':
                        word[i + j] = s2[j]
                    elif word[i + j] != s2[j]:
                        return ""

        # Step 2: Copy original state
        word2 = word[:]

        # Step 3: Process 'F' constraints
        for i in range(n):
            if s1[i] == 'F':
                cntBlank = 0
                cntSame = 0
                lastBlank = -1

                for j in range(m):
                    if word2[i + j] == '$':
                        if word[i + j] == '$':
                            word[i + j] = 'a'
                        lastBlank = i + j
                        cntBlank += 1

                    if word[i + j] == s2[j]:
                        cntSame += 1

                if cntSame == m and cntBlank == 0:
                    return ""

                if cntSame == m and cntBlank > 0:
                    word[lastBlank] = 'b'

        return ''.join(word)        