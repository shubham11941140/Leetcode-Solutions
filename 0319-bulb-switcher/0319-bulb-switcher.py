class Solution:

    def bulbSwitch(self, n: int) -> int:
        # initialize a variable count to 0
        count = 0
        # initialize a variable i to 1
        i = 1
        # while i*i is less than or equal to n
        while i * i <= n:
            # increment count by 1
            count += 1
            # increment i by 1
            i += 1
        # return the final value of count
        return int(sqrt(n))
        return count
