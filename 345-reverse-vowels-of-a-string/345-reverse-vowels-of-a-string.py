class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        l = 0
        r = len(s) - 1
        v = ['a', 'e', 'i', 'o', 'u']
        while l <= r:
            if s[l].lower() in v and s[r].lower() in v:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l].lower() in v:
                r -= 1
            elif s[r].lower() in v:
                l += 1
            else:
                l += 1
                r -= 1
        return ''.join(s)