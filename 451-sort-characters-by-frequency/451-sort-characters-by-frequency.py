from collections import Counter


class Solution:

    @staticmethod
    def frequencySort(s: str) -> str:
        d = Counter(s)
        a = sorted([(d[i], i) for i in d], reverse=True)
        return "".join([(v * k) for k, v in a])
