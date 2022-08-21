class Solution:

    @staticmethod
    def reverse(x: int) -> int:
        flag = False
        if x < 0:
            flag = True
        x = abs(x)
        s = list(str(x))[::-1]
        ans = int("".join(s))
        if len(bin(ans)[2:]) >= 32:
            return 0
        if flag:
            return -1 * ans
        return ans
