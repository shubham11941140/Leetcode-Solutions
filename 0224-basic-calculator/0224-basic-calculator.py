class Solution:

    def calculate(self, s: str) -> int:
        n = len(s)
        st = []
        num = 0
        sign = 1
        ans = 0
        for i in range(n):
            if s[i].isdigit():
                num = 10 * num + int(s[i])
            elif s[i] == "+":
                ans += sign * num
                num = 0
                sign = 1
            elif s[i] == "-":
                ans += sign * num
                num = 0
                sign = -1
            elif s[i] == "(":
                st.append(ans)
                st.append(sign)
                ans = 0
                sign = 1

            elif s[i] == ")":
                ans += sign * num
                num = 0
                ans *= st.pop()
                ans += st.pop()
        return ans + sign * num
