import numpy


class Solution:

    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []  # Return an empty array if it's impossible to reshape
        return numpy.reshape(original, (m, n)).tolist()
