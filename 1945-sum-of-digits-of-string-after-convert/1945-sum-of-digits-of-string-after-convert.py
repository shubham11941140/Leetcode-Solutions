class Solution:

    def getLucky(self, s: str, k: int) -> int:
        curr_str = "".join(str(ord(char) - ord("a") + 1) for char in s)
        for _ in range(k):
            curr_str = str(sum(int(char) for char in curr_str))
        return int(curr_str)
