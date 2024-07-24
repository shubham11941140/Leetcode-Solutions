class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mc = {}
        def get_mapped_value(num):
            if num not in mc:
                mc[num] = int(''.join(str(mapping[int(d)]) for d in str(num)))
            return mc[num]
        return sorted(nums, key = get_mapped_value)         