class Solution:                
        
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp, stack = [0] * (n + 1), []
        for i in range(n):
            if s[i] == ')':
                if stack:
                    idx = stack.pop()
                    dp[i + 1] = dp[idx] + (i - idx + 1)
            else:
                stack.append(i)
        return max(dp) if s else 0
            
                
        
