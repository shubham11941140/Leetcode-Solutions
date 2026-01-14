class Solution:

    def frequencySort(self, s: str) -> str:
        d = Counter(s)
        a = sorted([(d[i], i) for i in d], reverse=True)
        return "".join([(v * k) for k, v in a])
