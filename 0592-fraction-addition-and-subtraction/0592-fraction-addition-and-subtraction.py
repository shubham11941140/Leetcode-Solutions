from fractions import Fraction


class Solution:

    def fractionAddition(self, expression: str) -> str:
        fractions = expression.replace("-", "+-").split("+")
        result = sum(Fraction(f) for f in fractions if f)
        return f"{result.numerator}/{result.denominator}"
