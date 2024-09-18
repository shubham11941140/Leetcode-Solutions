class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Custom comparator to decide the order of concatenation
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        # Convert all numbers to strings for easy concatenation
        nums = list(map(str, nums))
        # Sort the numbers using the custom comparator
        nums.sort(key=cmp_to_key(compare))

        # Join the sorted numbers into a single string
        largest_num = ''.join(nums)

        # Edge case: if the largest number is '0', return '0'
        return '0' if largest_num[0] == '0' else largest_num        