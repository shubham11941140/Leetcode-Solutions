class Solution:
    def sortSentence(self, s: str) -> str:
        return ' '.join([y for x,y in sorted([(i[-1], i[:-1]) for i in s.split()])])
