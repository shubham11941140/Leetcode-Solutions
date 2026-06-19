class Solution:
    def longestCycle(self, edges: List[List[str]]) -> int:
        n = len(edges)
        bl = [False] * n
        mp = defaultdict(int)
        mx = -1
        for i in range(n):
            if not bl[i]:
                x = i
                l = 0
                st = set()
                while x > -1 and not bl[x]:
                    bl[x] = True
                    mp[x] = l
                    l += 1
                    st.add(x)
                    x = edges[x]
                if x != -1 and x in st:
                    mx = max(mx, l - mp[x])
        return mx
