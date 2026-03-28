class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = ["".join(sorted(i)) for i in strs]
        d = defaultdict(list)
        n = len(s)
        for i in range(n):
            d[s[i]].append(strs[i])
        return d.values()
