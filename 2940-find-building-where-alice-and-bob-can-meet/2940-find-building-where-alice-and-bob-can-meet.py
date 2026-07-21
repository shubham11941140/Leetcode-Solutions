class Solution:

    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        que = [[] for a in heights]
        h = []
        res = [-1] * len(queries)
        for qi, (i, j) in enumerate(queries):
            if i < j and heights[i] < heights[j]:
                res[qi] = j
            elif (i > j and heights[i] > heights[j]) or i == j:
                res[qi] = i
            else:
                que[max(i, j)].append([max(heights[i], heights[j]), qi])
        for i, a in enumerate(heights):
            while h and h[0][0] < a:
                res[heappop(h)[1]] = i
            for q in que[i]:
                heappush(h, q)
        return res
