class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        a = defaultdict(list)

        for u, v in adjacentPairs:
            a[u].append(v)
            a[v].append(u)

        ans = []
        for num, adjs in a.items():
            if len(adjs) == 1:
                ans.append(num)
                ans.append(adjs[0])
                break

        while len(ans) < len(adjacentPairs) + 1:
            tail = ans[-1]
            prev = ans[-2]
            adjs = a[tail]
            ans.append(adjs[0] if adjs[0] != prev else adjs[1])

        return ans
        