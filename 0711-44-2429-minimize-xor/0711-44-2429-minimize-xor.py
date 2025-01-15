class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Count the number of 1-bits in num2
        count_ones = bin(num2).count('1')        
        # Convert num1 to a list of its bits
        bits_num1 = list(bin(num1)[2:].zfill(32))        
        # Initialize the result with 0s
        result_bits = ['0'] * 32        
        # Try to set bits to 1 starting from the most significant bit
        for i in range(32):
            if not count_ones:
                break
            if bits_num1[i] == '1':
                result_bits[i] = '1'
                count_ones -= 1        
        # If there are still 1-bits to set, set them starting from the least significant bit
        for i in reversed(range(32)):
            if not count_ones:
                break
            if result_bits[i] == '0':
                result_bits[i] = '1'
                count_ones -= 1
        return int(''.join(result_bits), 2)     