class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        n = len(potions)

        def bsearch(s):
            left = 0
            right = n - 1
            pos = -1
            while left <= right:
                mid = (left + right) // 2
                if s * potions[mid] >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            return n - left

        return [bsearch(i) for i in spells]
