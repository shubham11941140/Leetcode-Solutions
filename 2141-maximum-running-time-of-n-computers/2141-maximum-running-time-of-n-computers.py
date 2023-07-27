class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def cannot_run(time):            
            return sum([min(t, time) for t in batteries]) < n * time        
        low, high = 0, sum(batteries) // n
        while low < high:
            guess = high - (high - low) // 2
            if cannot_run(guess):
                high = guess - 1
            else:
                low = guess
        return low      