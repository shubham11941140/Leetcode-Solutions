class Solution:

    def mirrorReflection(self, p: int, q: int) -> int:
        l = lcm(p, q)
        if not (l // q) % 2:
            return 2
        return (l // p) % 2
