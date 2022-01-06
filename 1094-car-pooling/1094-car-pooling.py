class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        val = [0] * 1005
        for i in range(len(trips)):
            for j in range(trips[i][1], trips[i][2]):
                val[j] += trips[i][0]
        return max(val) <= capacity
        