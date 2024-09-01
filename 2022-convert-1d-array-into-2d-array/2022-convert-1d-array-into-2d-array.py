import numpy


class Solution:

    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        return (
            [] if len(original) != m * n else numpy.reshape(original, (m, n)).tolist()
        )
