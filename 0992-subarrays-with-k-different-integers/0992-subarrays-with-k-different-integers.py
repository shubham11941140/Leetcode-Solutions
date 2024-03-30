class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(A, K):
            count = Counter()
            res = i = 0
            for j in range(len(A)):
                if not count[A[j]]: 
                    K -= 1
                count[A[j]] += 1
                while K < 0:
                    count[A[i]] -= 1
                    if not count[A[i]]: 
                        K += 1
                    i += 1
                res += j - i + 1
            return res

        return atMostK(nums, k) - atMostK(nums, k - 1)        