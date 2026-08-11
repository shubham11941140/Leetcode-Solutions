class Solution:

    def numberOfSubstrings(self, s: str) -> int:
        count = {"a": 0, "b": 0, "c": 0}
        start = 0
        result = 0
        for end in range(len(s)):
            count[s[end]] += 1
            while count["a"] > 0 and count["b"] > 0 and count["c"] > 0:
                result += len(s) - end
                count[s[start]] -= 1
                start += 1
        return result
