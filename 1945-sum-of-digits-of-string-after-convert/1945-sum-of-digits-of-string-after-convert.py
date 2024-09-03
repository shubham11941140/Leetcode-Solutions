class Solution:

    def getLucky(self, s: str, k: int) -> int:
        # Convert the string to a number formed by the position in the alphabet
        num_str = "".join(str(ord(char) - ord("a") + 1) for char in s)

        # Start with the massive number string
        curr_str = num_str

        # Perform the sum of digits process k times
        for _ in range(k):
            curr_str = str(sum(int(char) for char in curr_str))

        return int(curr_str)
