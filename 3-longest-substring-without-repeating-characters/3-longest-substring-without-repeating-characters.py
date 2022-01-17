class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window solution
        n = len(s)
        a = []
        i = 0
        ans = 0
        while i < n:
            if s[i] not in a:
                a.append(s[i])
                i += 1
            else:
                a.pop(0)
            ans = max(ans, len(a))
        print(ans)
        return ans
                
            
            
        