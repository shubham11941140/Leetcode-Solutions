class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        gap = [startTime[0]] + [startTime[i] - endTime[i - 1] for i in range(1, len(startTime))] + [eventTime - endTime[-1]]
        largestRight = [0] * len(gap)
        for i in reversed(range(len(gap) - 1)):
            largestRight[i] = max(largestRight[i + 1], gap[i + 1])

        ans = 0
        largestLeft = 0
        for i in range(1, len(gap)):
            curGap = endTime[i - 1] - startTime[i - 1]
            if curGap <= max(largestLeft, largestRight[i]):
                ans = max(ans, gap[i - 1] + gap[i] + curGap)
            ans = max(ans, gap[i - 1] + gap[i])
            largestLeft = max(largestLeft, gap[i - 1])
        return ans