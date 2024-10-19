class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def build_string(n):
            if n == 1:
                return "0"
            prev = build_string(n - 1)
            return prev + "1" + ''.join('1' if c == '0' else '0' for c in prev)[::-1]
        return build_string(n)[k - 1]

        