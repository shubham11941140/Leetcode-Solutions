class Solution:

    def minimumLength(self, s: str) -> int:
        return sum(2 - (x % 2) for x in Counter(s).values())
