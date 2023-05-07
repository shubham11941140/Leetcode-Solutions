class Solution:

    def longestObstacleCourseAtEachPosition(self,
                                            obstacles: List[int]) -> List[int]:
        v, ans = [], []
        for i in range(len(obstacles)):
            it = bisect.bisect_right(v, obstacles[i])
            if it == len(v):
                v.append(obstacles[i])
                ans.append(len(v))
            else:
                v[it] = obstacles[i]
                ans.append(it + 1)
        return ans
