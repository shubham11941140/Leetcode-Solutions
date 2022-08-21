class Solution:

    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n, m = len(stamp), len(target)
        s = {
            "#" * i + stamp[i:n - j] + "#" * j
            for i in range(n) for j in range(n - i)
        }
        end = "#" * m
        r = []
        while target != end:
            c = False
            for i in reversed(range(m - n + 2)):
                if target[i:i + n] in s:
                    target = target[:i] + "#" * n + target[i + n:]
                    r.append(i)
                    c = True
            if not c:
                return []
        return r[::-1]
