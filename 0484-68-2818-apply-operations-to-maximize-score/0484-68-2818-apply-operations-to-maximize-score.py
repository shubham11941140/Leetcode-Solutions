class Solution:

    def maximumScore(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        n = len(nums)
        prime_scores = [0] * n
        l = [0] * n
        r = [0] * n

        for i in range(n):
            count = 0
            number = nums[i]
            prime = 2
            while prime * prime <= number:
                if number % prime == 0:
                    count += 1
                    while number % prime == 0:
                        number //= prime
                prime += 1
            if number > 1:
                count += 1
            prime_scores[i] = count

        stack = [n - 1]
        l[n - 1] = n - 1
        for i in reversed(range(n - 1)):
            while stack and prime_scores[stack[-1]] <= prime_scores[i]:
                stack.pop()
            l[i] = n - 1 if not stack else stack[-1] - 1
            stack.append(i)

        stack = [0]
        r[0] = 0
        for i in range(1, n):
            while stack and prime_scores[stack[-1]] < prime_scores[i]:
                stack.pop()
            r[i] = 0 if not stack else stack[-1] + 1
            stack.append(i)

        s = sorted([(nums[i], i) for i in range(n)])

        total_score = 1
        for i in reversed(range(n)):
            if k <= 0:
                break
            t = (l[s[i][1]] - s[i][1] + 1) * (s[i][1] - r[s[i][1]] + 1)
            total_score *= pow(s[i][0], min(k, t), mod)
            k -= t

        return total_score % mod
