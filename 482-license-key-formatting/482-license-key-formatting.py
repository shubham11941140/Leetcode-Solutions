class Solution:

    def licenseKeyFormatting(self, s: str, k: int) -> str:
        a = list(s.upper())
        while "-" in a:
            a.remove("-")
        a = a[::-1]
        ans = ""
        for i in range(len(a)):
            ans += a[i]
            if (i + 1) % k == 0 and i != len(a) - 1:
                ans += "-"
        return "".join(ans[::-1])
