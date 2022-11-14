class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        if not n:
            return 0
        m1 = defaultdict(list)
        m2 = defaultdict(list)
        for i in range(n):
            m1[stones[i][0]].append(i)
            m2[stones[i][1]].append(i)
        ans = 0
        st = []
        vis = [False] * n
        for i in range(n):
            if vis[i]:
                continue
            st.append(i)
            vis[i] = True
            while st:
                x = st.pop()
                for y in m1[stones[x][0]]:
                    if not vis[y]:
                        vis[y] = True
                        st.append(y)
                for y in m2[stones[x][1]]:
                    if not vis[y]:
                        vis[y] = True
                        st.append(y)
            ans += 1
        return n - ans
