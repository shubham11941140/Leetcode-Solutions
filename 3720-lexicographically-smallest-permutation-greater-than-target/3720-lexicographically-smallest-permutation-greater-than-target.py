class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26
        for i in range(len(s)):
            cnt[ord(s[i]) - ord("a")] += 1
            cnt[ord(target[i]) - ord("a")] -= 1

        # Try from right to left
        t = list(target)
        for i in reversed(range(len(s))):
            b = ord(t[i]) - ord("a")
            cnt[b] += 1  # Reversal of consumption
            # Check if the prefix can fully match
            if min(cnt) < 0:
                continue
            # Find the smallest available character larger than b.
            for j in range(b + 1, 26):
                if cnt[j] > 0:
                    cnt[j] -= 1
                    t[i] = chr(ord("a") + j)
                    return "".join(t[: i + 1]) + "".join([chr(ord("a") + i) * cnt[i] for i in range(26)])
        return "" 