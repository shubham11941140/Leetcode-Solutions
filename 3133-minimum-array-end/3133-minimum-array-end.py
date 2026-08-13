class Solution:

    def minEnd(self, n: int, x: int) -> int:
        ans = 0
        j = 0
        for i in range(56):  # Limit to 56 bits, as in the original C++ code
            if (x >> i) & 1:  # Check if the i-th bit in X is set
                ans |= 1 << i  # Set the i-th bit in ans to 1
            else:
                if ((n - 1) >> j) & 1:  # Use bits from N sequentially
                    ans |= 1 << i  # Set the i-th bit in ans according to N
                j += 1  # Move to the next bit in N only if X[i] was not set
        return ans
