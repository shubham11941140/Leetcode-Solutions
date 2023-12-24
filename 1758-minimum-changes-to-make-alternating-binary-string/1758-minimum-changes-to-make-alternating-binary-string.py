class Solution:
    def minOperations(self, s: str) -> int:
        changes1, changes2 = 0, 0  # Count changes for "0101..." and "1010..." patterns

        # Iterate over the string
        for i in range(len(s)):
            if i % 2 == 0:  # For even indices
                if s[i] != '0':
                    changes1 += 1
                if s[i] != '1':
                    changes2 += 1
            else:  # For odd indices
                if s[i] != '1':
                    changes1 += 1
                if s[i] != '0':
                    changes2 += 1

        # Return the minimum number of changes
        return min(changes1, changes2)        