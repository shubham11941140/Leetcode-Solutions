class Solution:

    @staticmethod
    def carPooling(trips: List[List[int]], capacity: int) -> bool:
        val = [0] * 1005
        for i, item in enumerate(trips):
            for j in range(item[1], item[2]):
                val[j] += item[0]
        return max(val) <= capacity
