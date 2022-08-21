class Solution:

    @staticmethod
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        s = ["".join(sorted(i)) for i in strs]
        d = {}
        n = len(s)
        for i in range(n):
            if s[i] in d:
                d[s[i]].append(strs[i])
            else:
                d[s[i]] = [strs[i]]
        return d.values()
