from math import comb


class Solution:

    def idealArrays(self, n: int, maxValue: int) -> int:
        total_ways = maxValue
        frequency_map = {num: 1 for num in range(1, maxValue + 1)}
        for array_size in range(1, n):
            new_frequency = Counter()
            for base_value in frequency_map:
                for multiplier in range(2, maxValue // base_value + 1):
                    total_ways += comb(n - 1, array_size) * \
                        frequency_map[base_value]
                    new_frequency[multiplier *
                                  base_value] += frequency_map[base_value]
            frequency_map = new_frequency
            total_ways %= 10**9 + 7
        return total_ways
