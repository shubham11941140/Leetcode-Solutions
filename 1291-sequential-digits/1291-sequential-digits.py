class Solution:

    @staticmethod
    def gen():
        a = list(range(1, 10))
        return [
            a[i:j] for i in range(9) for j in range(i, 10) if len(a[i:j]) > 1
        ]

    @staticmethod
    def process(b):
        return [int(i) for i in ["".join([str(k) for k in a]) for a in b]]

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        d = self.process(self.gen())
        return sorted([d[i] for i in range(len(d)) if low <= d[i] <= high])
