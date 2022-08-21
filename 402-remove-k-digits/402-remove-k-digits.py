class Solution:

    def call(self, a, s, k):
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

    def new(self, num, k):
        s = list(num).copy()
        while k:
            if s[0] < s[1]:
                s.remove(s[1])
            else:
                s.remove(s[0])
            k -= 1
        return "".join(s)

    def removeKdigits(self, num: str, k: int) -> str:
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

        if len(num) == k:
            return "0"
        v = self.new(num, k)

        a = list(range(10))[::-1]
        a = [str(i) for i in a]
        s = list(num)
        ret = "9" * (10**6)
        for i in range(10):
            l = s.copy()
            v1 = self.call(a[i:], l, k)
            if len(v1) == len(s) - k:
                if v1 < ret:
                    ret = v1
        if not ret or not v:
            return "0"
        print("V", v)
        print("RET", ret)
        return str(min(int(ret), int(v)))
