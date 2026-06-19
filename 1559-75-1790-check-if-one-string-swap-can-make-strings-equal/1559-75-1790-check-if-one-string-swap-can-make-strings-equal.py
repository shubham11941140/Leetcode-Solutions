class Solution:

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # If the strings are already equal, return True
        if s1 == s2:
            return True
        # Find the positions where the characters are different
        diff = [i for i in range(len(s1)) if s1[i] != s2[i]]
        # If there are not exactly two differences, return False
        if len(diff) != 2:
            return False
        # Check if swapping the two differing characters makes the strings equal
        i, j = diff
        return s1[i] == s2[j] and s1[j] == s2[i]
