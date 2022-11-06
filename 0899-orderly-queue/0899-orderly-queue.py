class Solution:

    def orderlyQueue(self, s: str, k: int) -> str:
        S = s
        K = k
        if K == 1:
            return min(S[i:] + S[:i] for i in range(len(S)))
        return "".join(sorted(S))
