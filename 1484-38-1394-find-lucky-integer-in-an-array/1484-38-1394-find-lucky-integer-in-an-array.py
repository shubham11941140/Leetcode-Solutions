class Solution:

    def findLucky(self, arr: List[int]) -> int:
        d = [k for k, v in Counter(arr).items() if k == v]
        return max(d) if d else -1
