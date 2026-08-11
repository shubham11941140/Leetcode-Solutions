class Solution:

    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_sum = mean * (n + m)
        current_sum = sum(rolls)
        missing_sum = total_sum - current_sum

        if missing_sum < n or missing_sum > 6 * n:
            return []

        quotient, remainder = divmod(missing_sum, n)
        result = [quotient] * n

        for i in range(remainder):
            result[i] += 1

        return result
