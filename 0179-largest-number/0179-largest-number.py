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

        largest_num = "".join(sorted(list(map(str, nums)), key=cmp_to_key(compare)))
        return "0" if largest_num[0] == "0" else largest_num
