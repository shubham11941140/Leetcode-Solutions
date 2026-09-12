class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int],
                            worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        ans = i = best = 0
        for ability in worker:
            while i < len(jobs) and ability >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            ans += best
        return ans
