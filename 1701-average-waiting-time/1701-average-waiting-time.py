class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait = 0
        curr = 0
        for arrival_i, time_i in customers:
            curr = max(curr, 1.0 * arrival_i) + time_i
            wait += curr - arrival_i
        return wait / len(customers)        