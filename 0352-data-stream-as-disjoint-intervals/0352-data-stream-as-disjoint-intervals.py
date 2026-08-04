class SummaryRanges:

    def __init__(self):
        self.s = []

    def addNum(self, value: int) -> None:
        self.s.append(value)

    def getIntervals(self) -> List[List[int]]:
        self.s = sorted(list(set(self.s)))
        start = self.s[0]
        end = self.s[0]
        res = []
        for i in range(1, len(self.s)):
            if self.s[i] == end + 1:
                end = self.s[i]
            else:
                res.append([start, end])
                start = self.s[i]
                end = self.s[i]
        res.append([start, end])
        return res


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
