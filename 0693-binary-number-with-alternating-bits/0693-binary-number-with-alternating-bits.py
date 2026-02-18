class Solution:
    def hasAlternatingBits(self, n: int) -> bool:      
        return False if bin(n).find('11') + 1 or bin(n).find('00') + 1 else True   