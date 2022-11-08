class Solution:
    def makeGood(self, s: str) -> str:
        st = []
        for ch in s:
            if st and abs(ord(ch) - ord(st[-1])) == 32:
                st.pop()
            else:
                st.append(ch)
        return ''.join(st)        