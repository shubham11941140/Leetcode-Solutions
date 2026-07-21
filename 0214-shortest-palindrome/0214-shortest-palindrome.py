class Solution:

    def shortestPalindrome(self, s: str) -> str:
        rev_s = s[::-1]
        new_s = s + "#" + rev_s
        # Compute the KMP table (partial match table)
        n = len(new_s)
        lps = [0] * n
        j = 0  # length of the previous longest prefix suffix
        for i in range(1, n):
            while j > 0 and new_s[i] != new_s[j]:
                j = lps[j - 1]
            if new_s[i] == new_s[j]:
                j += 1
                lps[i] = j
        return rev_s[: len(s) - lps[-1]] + s
