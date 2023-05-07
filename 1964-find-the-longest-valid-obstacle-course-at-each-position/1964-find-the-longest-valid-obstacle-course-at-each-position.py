class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        v, ans = [], []
        for i in obstacles:
            it = bisect.bisect_right(v, i)
            if it == len(v):
                v.append(i)
                ans.append(len(v))
            else:
                v[it] = i
                ans.append(it + 1)
        return ans        