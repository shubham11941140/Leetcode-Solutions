class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @lru_cache(None)
        def compute(expr: str) -> List[int]:
            if expr.isdigit():
                return [int(expr)]            
            results = []
            for i, char in enumerate(expr):
                if char in "+-*":                   
                    for left in compute(expr[:i]):
                        for right in compute(expr[i + 1:]):
                            if char == '+':
                                results.append(left + right)
                            elif char == '-':
                                results.append(left - right)
                            elif char == '*':
                                results.append(left * right)
            return results        
        return compute(expression)        