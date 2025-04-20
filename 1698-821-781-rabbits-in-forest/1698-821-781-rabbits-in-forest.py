class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        return sum([((j + i) // (i + 1) * (i + 1)) for i, j in Counter(answers).items()])      