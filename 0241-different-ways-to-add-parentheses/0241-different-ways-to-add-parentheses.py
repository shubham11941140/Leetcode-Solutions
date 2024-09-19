class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @lru_cache(None)
        def compute(expr: str) -> List[int]:
            if expr.isdigit():
                return [int(expr)]
            
            results = []
            for i, char in enumerate(expr):
                if char in "+-*":
                    left_results = compute(expr[:i])
                    right_results = compute(expr[i+1:])
                    
                    for left in left_results:
                        for right in right_results:
                            if char == '+':
                                results.append(left + right)
                            elif char == '-':
                                results.append(left - right)
                            elif char == '*':
                                results.append(left * right)
            return results
        
        return compute(expression)        