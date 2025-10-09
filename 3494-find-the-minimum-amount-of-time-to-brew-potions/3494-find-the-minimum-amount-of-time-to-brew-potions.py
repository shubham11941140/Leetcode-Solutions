class Solution:

    def minTime(self, skills: List[int], energy: List[int]) -> int:
        n, m = len(skills), len(energy)
        p = [0] * n
        for i in range(1, n):
            p[i] = p[i - 1] + skills[i]

        total_time = skills[0] * energy[0]

        for j in range(1, m):
            max_time = skills[0] * energy[j]
            for i in range(1, n):
                diff_time = p[i] * energy[j - 1] - p[i - 1] * energy[j]
                if diff_time > max_time:
                    max_time = diff_time
            total_time += max_time

        return total_time + p[-1] * energy[-1]
