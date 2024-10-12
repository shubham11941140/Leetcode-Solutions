class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        events = defaultdict(int)
        for start, end in intervals:
            events[start] += 1
            events[end + 1] -= 1
        ongoing_intervals = 0
        max_intervals = 0
        for time in sorted(events.keys()):
            ongoing_intervals += events[time]
            max_intervals = max(max_intervals, ongoing_intervals)
        return max_intervals        