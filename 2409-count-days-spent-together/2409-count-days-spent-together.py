class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        return max(0, self.getDate(min(leaveAlice, leaveBob)) - self.getDate(max(arriveAlice, arriveBob)) + 1)
    
    def getDate(self, date):
        monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return sum(monthList[:int(date[:2]) - 1]) + int(date[3:])