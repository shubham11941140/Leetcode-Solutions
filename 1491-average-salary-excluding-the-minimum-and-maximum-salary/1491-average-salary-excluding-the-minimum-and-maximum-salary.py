class Solution:

    @staticmethod
    def average(salary: List[int]) -> float:
        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)
