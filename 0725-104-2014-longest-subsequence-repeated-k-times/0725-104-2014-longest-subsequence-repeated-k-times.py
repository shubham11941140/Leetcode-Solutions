class Solution:
    def solve(self, sub: str, s: str, k: int) -> bool:
        i = cnt = 0
        for ch in s:
            if ch == sub[i]:
                i += 1
                if i == len(sub):
                    cnt += 1
                    i = 0
                    if cnt == k:
                        return True
        return False    
    
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        ans = ""
        q = deque([""])
        while q:
            curr = q.popleft()
            for ch in map(chr, range(ord('a'), ord('z') + 1)):
                next_sub = curr + ch
                if self.solve(next_sub, s, k):
                    ans = next_sub
                    q.append(next_sub)
        return ans        