class Solution:

    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        a = []
        for num in nums:
            i = bisect_left(arr, num)
            a.append(i)
            del arr[i]
        return a
