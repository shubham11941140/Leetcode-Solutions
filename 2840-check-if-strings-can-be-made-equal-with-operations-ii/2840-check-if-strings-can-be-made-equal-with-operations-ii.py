class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        eX = oX = eS = oS = 0

        for i, (a, b) in enumerate(zip(s1, s2)):
            v1 = ord(a)
            v2 = ord(b)
            dx = v1 ^ v2
            ds = v1 * v1 - v2 * v2

            if i & 1:
                oX ^= dx
                oS += ds
            else:
                eX ^= dx
                eS += ds

        return not (eX | oX | eS | oS)        