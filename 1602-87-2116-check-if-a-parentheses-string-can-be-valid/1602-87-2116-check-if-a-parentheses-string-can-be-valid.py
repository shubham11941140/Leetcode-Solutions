class Solution:

    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2:
            # If the length of s is odd, it's impossible to have a valid parentheses string
            return False
        # Check the balance of the parentheses from left to right
        oc = 0
        for i in range(n):
            oc += 1 if s[i] == "(" or locked[i] == "0" else -1
            if oc < 0:
                return False
        # Check the balance of the parentheses from right to left
        cc = 0
        for i in reversed(range(n)):
            cc += 1 if s[i] == ")" or locked[i] == "0" else -1
            if cc < 0:
                return False
        return True
