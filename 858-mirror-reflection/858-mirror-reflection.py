class Solution:

    @staticmethod
    def mirrorReflection(p: int, q: int) -> int:
        l = lcm(p, q)
        if not (l // q) % 2:
            return 2
        return (l // p) % 2
