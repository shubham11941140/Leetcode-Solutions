class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cc = Counter(s)
        sc = []
        for char in order:
            sc.append(char * cc[char])
            cc[char] = 0
        return "".join(sc + [char * count for char, count in cc.items()])
