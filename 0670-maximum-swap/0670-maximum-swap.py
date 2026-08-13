class Solution:

    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        max_num = num
        # Try swapping each pair of digits and keep track of the max number
        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                # Swap digits
                digits[i], digits[j] = digits[j], digits[i]
                # Convert list of digits back to number
                new_num = int("".join(digits))
                # Update max number if new number is greater
                if new_num > max_num:
                    max_num = new_num
                # Swap back to original positions
                digits[i], digits[j] = digits[j], digits[i]
        return max_num
