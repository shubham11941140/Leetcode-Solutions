class Solution:
    def sortVowels(self, s: str) -> str:
        if not s:
            return ""
        vowels = set("aeiouAEIOU")
        n = len(s)
        r = [" " for i in range(n)]
        a = sorted([s[i] for i in range(n) if s[i] in vowels])
        for i in range(n):
            if s[i] not in vowels:
                r[i] = s[i]
        j = 0
        for i in range(n):
            if r[i] == " ":
                r[i] = a[j]
                j += 1
        return "".join(r)
