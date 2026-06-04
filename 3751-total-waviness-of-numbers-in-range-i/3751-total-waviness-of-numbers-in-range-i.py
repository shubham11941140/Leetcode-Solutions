class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        return sum(p * q < 0 for v in range(num1, num2 + 1) 
            for p, q in pairwise(starmap(sub, pairwise(map(int, str(v))))))