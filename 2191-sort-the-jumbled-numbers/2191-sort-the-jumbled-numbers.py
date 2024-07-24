class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped_cache = {}

        def get_mapped_value(num):
            if num not in mapped_cache:
                mapped_str = ''.join(str(mapping[int(digit)]) for digit in str(num))
                mapped_cache[num] = int(mapped_str)
            return mapped_cache[num]

        # Sort nums based on their mapped values
        nums.sort(key=get_mapped_value)

        return nums        

        
        
        def get_mapped_value(num):
            return int(''.join(str(mapping[int(digit)]) for digit in str(num)))

        # Create a list of tuples (mapped_value, original_value)
        mapped_nums = [(get_mapped_value(num), num) for num in nums]

        # Sort based on the mapped values, and if they are the same, maintain the original order
        mapped_nums.sort(key=lambda x: (x[0], nums.index(x[1])))

        # Extract the original values in the new sorted order
        sorted_nums = [num for _, num in mapped_nums]

        return sorted_nums        