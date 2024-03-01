class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # Count the number of '1's in the binary string
        count_ones = s.count("1")

        # If there are no '1's, there's no odd number possible, return empty string
        if count_ones == 0:
            return ""

        # Otherwise, construct the maximum odd binary number by doing the following:
        # - Use all '1's except one to maintain oddness ('1' * (count_ones - 1))
        # - Fill the rest of the string with '0's ((len(s) - count_ones) * "0")
        # - Add a '1' at the end to ensure the number is odd
        return "1" * (count_ones - 1) + (len(s) - count_ones) * "0" + "1"
