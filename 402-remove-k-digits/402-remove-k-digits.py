class Solution:

    @staticmethod
    def call(a, s, k):
        h = 0
        for i in a:
            while i in s:
                s.remove(i)
                h += 1
                if h == k:
                    break
            if h == k:
                break
        return "".join(s)

    @staticmethod
    def new(num, k):
        s = list(num).copy()
        while k:
            if s[0] < s[1]:
                s.remove(s[1])
            else:
                s.remove(s[0])
            k -= 1
        return "".join(s)

    @staticmethod
    def removeKdigits(num: str, k: int) -> str:
        st = []
        for n in num:
            while st and k and st[-1] > n:
                st.pop()
                k -= 1
            if st or n is not "0":
                st.append(n)
        if k:
            st = st[0:-k]
        return "".join(st) or "0"
