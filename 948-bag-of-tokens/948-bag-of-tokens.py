class Solution:

    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)
        l = 0
        r = n - 1
        s = 0
        ans = 0
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                s += 1
                l += 1
            elif power < tokens[l] and s >= 1:
                power += tokens[r]
                r -= 1
                s -= 1
            else:
                break
            ans = max(ans, s)
        return ans
