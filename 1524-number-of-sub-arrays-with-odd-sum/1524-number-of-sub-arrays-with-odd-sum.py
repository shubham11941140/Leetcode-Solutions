class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd_count, even_count = 0, 1
        prefix_sum = 0
        result = 0       
        for num in arr:
            prefix_sum += num
            if prefix_sum % 2:
                result += even_count  # If odd, add previously seen even prefix sums
                odd_count += 1
            else:
                result += odd_count  # If even, add previously seen odd prefix sums
                even_count += 1    
        return result % (10 ** 9 + 7)