class Solution:

    @staticmethod
    def sortSentence(s: str) -> str:
        return " ".join(
            [y for x, y in sorted([(i[-1], i[:-1]) for i in s.split()])])
