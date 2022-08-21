class Solution:

    def maxDistToClosest(self, seats: List[int]) -> int:
        a = [i for i in range(len(seats)) if seats[i]]
        return max([(a[i] - a[i - 1]) // 2 for i in range(1, len(a))] +
                   [a[0]] + [len(seats) - 1 - a[-1]])
