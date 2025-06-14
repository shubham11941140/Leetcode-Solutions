class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        
        # Find the first non-nine digit for max transformation
        for digit in s:
            if digit != '9':
                max_num = s.replace(digit, '9')
                break
        else:
            max_num = s  # If all digits are 9, no change needed
        
        # Find the first digit for min transformation
        min_num = s.replace(s[0], '0')
        
        return int(max_num) - int(min_num)      