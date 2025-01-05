class Solution:

    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift = [0] * (n + 1)
        # Apply the shifts
        for start, end, direction in shifts:
            if direction == 1:
                shift[start] += 1
                if end + 1 < n:
                    shift[end + 1] -= 1
            else:
                shift[start] -= 1
                if end + 1 < n:
                    shift[end + 1] += 1
        # Calculate the net shifts
        for i in range(1, n):
            shift[i] += shift[i - 1]
        # Shift the characters
        return "".join(
            [chr((ord(s[i]) - ord("a") + shift[i]) % 26 + ord("a"))
             for i in range(n)]
        )
