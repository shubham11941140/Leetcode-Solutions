class Solution:

    def findKthBit(self, n: int, k: int) -> str:

        def build_string(n):
            if n == 1:
                return "0"
            prev = build_string(n - 1)
            inverted = "".join("1" if c == "0" else "0" for c in prev)
            return prev + "1" + inverted[::-1]

        binary_string = build_string(n)
        return binary_string[k - 1]
