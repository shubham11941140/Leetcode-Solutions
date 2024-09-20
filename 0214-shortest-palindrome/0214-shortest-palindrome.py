class Solution:

    def shortestPalindrome(self, s: str) -> str:
        # Create a new string which is the original string + a special character + the reverse of the original string
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

        # The length of the longest palindromic prefix
        longest_palindromic_prefix_len = lps[-1]

        # Add the necessary characters in front of the original string
        add_on = rev_s[: len(s) - longest_palindromic_prefix_len]
        return add_on + s
