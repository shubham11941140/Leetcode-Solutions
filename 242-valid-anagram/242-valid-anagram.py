from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        return len(s) == len(t) and set(s) == set(t) and Counter(s) == Counter(t)
        