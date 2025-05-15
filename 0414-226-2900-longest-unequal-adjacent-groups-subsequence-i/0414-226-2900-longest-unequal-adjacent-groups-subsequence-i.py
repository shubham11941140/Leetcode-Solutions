class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        return [x for i, x in enumerate(words) if not i or groups[i] != groups[i - 1]]