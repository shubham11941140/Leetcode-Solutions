class Solution:

    def validateCoupons(self, code: List[str], businessLine: List[str],
                        isActive: List[bool]) -> List[str]:
        return [
            c for c, _ in sorted(
                ((c, b) for c, b, a in zip(code, businessLine, isActive)
                 if a and c and bool(re.fullmatch(r"[A-Za-z0-9_]+", c)) and b
                 in ["electronics", "grocery", "pharmacy", "restaurant"]),
                key=lambda x: (x[1], x[0]),
            )
        ]
