class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        q = deque()
        q.append((start, 0))
        while q:
            s, c = q.popleft()
            if s == end:
                return c
            for i in range(len(s)):
                for j in "ACGT":
                    if s[i] != j:
                        ns = s[:i] + j + s[i + 1:]
                        if ns in bank:
                            bank.remove(ns)
                            q.append((ns, c + 1))
        return -1        