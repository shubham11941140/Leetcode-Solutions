class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t = 0
        n = len(tickets)
        while True:
            for i in range(n):
                if tickets[i]:
                    tickets[i] -= 1
                    t += 1
                    if tickets[k] == 0:
                        return t
        