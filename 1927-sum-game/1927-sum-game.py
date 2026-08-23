class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        leftQ = len([i for i in range(n // 2) if num[i] == '?'])
        leftSum = sum([int(num[i]) for i in range(n // 2) if num[i] != '?'])
        rightSum = sum([int(num[i]) for i in range(n // 2, n) if num[i] != '?'])
        return (leftSum - rightSum) * 2 != (num.count('?') - 2 * leftQ) * 9