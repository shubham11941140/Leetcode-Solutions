from math import ceil, sqrt


class Solution:

    def __init__(self):
        self.a = []
        self.b = []

    @staticmethod
    def isprime(n):
        if n == 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, ceil(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def createPalindrome(inp, b, isOdd):
        n = inp
        palin = inp
        if isOdd:
            n = n // b
        while n > 0:
            palin = palin * b + (n % b)
            n = n // b
        return palin

    def generatePalindromes(self, n):
        for j in range(2):
            i = 1
            while self.createPalindrome(i, 10, j % 2) < n:
                self.a.append(self.createPalindrome(i, 10, j % 2))
                i = i + 1

    def gen(self):
        n = 10**8 + 10**6
        self.generatePalindromes(n)
        self.b = sorted([i for i in self.a if self.isprime(i)])

    def primePalindrome(self, n: int) -> int:
        self.gen()
        for i in self.b:
            if i >= n:
                return i
