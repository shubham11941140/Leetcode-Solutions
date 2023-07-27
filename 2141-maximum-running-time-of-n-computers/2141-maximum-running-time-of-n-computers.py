class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def cannot_run(n,batteries,time):
            curr_sum =0
            for t in batteries:
                curr_sum += min(t, time)
            return curr_sum <n *time
        
        low,high =0,sum(batteries)// n
        while low <high:
            guess =high -(high -low)// 2 # prevent infinite loop to find the maximal T
            if cannot_run(n,batteries,guess):
                high =guess -1
            else:
                low =guess
        return low      