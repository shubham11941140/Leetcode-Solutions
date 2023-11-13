class Solution:
    def sortVowels(self, s: str) -> str:
        if not s:
            return ""
        vowels = set("aeiouAEIOU")
        n = len(s)
        r = [" " for i in range(n)]
        a = []
        for i in range(n):
            if s[i] not in vowels:
                r[i] = s[i]
            else:
                a.append(s[i])
        a.sort()
        print(a)
        j = 0
        for i in range(n):
            if r[i] == " ":
                r[i] = a[j]
                j += 1
        return "".join(r)