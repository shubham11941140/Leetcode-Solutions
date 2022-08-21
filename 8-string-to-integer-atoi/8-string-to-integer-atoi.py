class Solution:

    def remw(self, s):
        n = len(s)
        i = 0
        while s[i] == " ":
            i += 1
            if i == n:
                break
        return s[i:]

    def myAtoi(self, s: str) -> int:

        if not s:
            return 0

        s = self.remw(s)

        if not s:
            return 0

        flag = 1

        if "+-" in s or "-+" in s or "++" in s[:2] or "--" in s[:2]:
            return 0

        if s[0] == "+":
            s = s.replace("+", "")

        if not s:
            return 0

        if s[0] == "-":
            flag = -1
            s = s.replace("-", "")

        if not s:
            return 0

        if s[0].isdigit():
            i = 0
            n = len(s)

            while s[i].isdigit():
                i += 1
                if i == len(s):
                    break

            t = s[:i]
            val = flag * int("".join(t))

            if val < -1 * (2**31):
                return -1 * (2**31)
            if val >= 2**31:
                return 2**31 - 1
            return val
        return 0
