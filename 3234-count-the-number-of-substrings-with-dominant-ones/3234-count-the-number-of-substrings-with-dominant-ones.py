class Solution:

    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        result = 0
        # Iterate through possible zero counts (1 to sqrt(n))
        for k in range(1, int(n**0.5) + 1):
            zeros = deque()  # Queue to store positions of zeros
            l = -1  # r window
            ones = 0  # Count of ones in our current window
            for right in range(n):
                if s[right] == "0":
                    zeros.append(right)
                    # If we have more than k zeros, remove the leftmost one
                    while len(zeros) > k:
                        ones -= zeros[0] - l - 1  # Subtr
                        l = zeros.popleft()
                else:
                    ones += 1
                if len(zeros) == k and ones >= k**2:
                    result += min(zeros[0] - l, ones - k**2 + 1)
        # Handle all-ones substrings
        i = 0
        while i < n:
            if s[i] == "0":
                i += 1
                continue
            sz = 0
            while i < n and s[i] == "1":
                sz += 1
                i += 1
            result += (sz * (sz + 1)) // 2
        return result
