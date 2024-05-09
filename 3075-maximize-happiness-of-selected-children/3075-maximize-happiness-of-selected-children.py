class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        indx = 0
        t = 0
        while k > 0:
            happiness[indx] = max(happiness[indx] - indx, 0)
            t += happiness[indx]
            indx += 1
            k -= 1
        return t       