class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        l = 0
        r = 0
        ans = 0
        cnt = 0
        while r < n:
            if answerKey[r] == 'F':
                cnt += 1
            while cnt > k:
                if answerKey[l] == 'F':
                    cnt -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        l = 0
        r = 0
        cnt = 0
        while r < n:
            if answerKey[r] == 'T':
                cnt += 1
            while cnt > k:
                if answerKey[l] == 'T':
                    cnt -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans        