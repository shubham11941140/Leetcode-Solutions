class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for time in timePoints:
            h, m = map(int, time.split(':'))
            minutes.append(h * 60 + m)
        minutes.sort()
        return min(min([minutes[i] - minutes[i - 1] for i in range(1, len(minutes))]), 1440 + minutes[0] - minutes[-1])       