class Solution:
    @staticmethod
    def reverseWords(s: str) -> str:
        return ' '.join(s.split()[::-1])
