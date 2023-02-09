class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        h = defaultdict(set)
        for w in ideas:
            h[w[0]].add(w[1:])

        res = 0
        for char1 in h:
            for char2 in h:
                if char1 == char2:
                    continue
                intersect = 0

                for w in h[char1]:
                    if w in h[char2]:
                        intersect += 1

                d1 = len(h[char1]) - intersect
                d2 = len(h[char2]) - intersect

                res += d1 * d2
        return res
