class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        p = int(''.join([str(i) for i in digits]))
        return [int(i) for i in str(p + 1)]
    
        