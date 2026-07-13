class Solution:                         
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        a = list(range(1, 10))
        b = [a[i:j] for i in range(9) for j in range(i, 10) if len(a[i:j]) > 1]        
        d = [int(i) for i in [''.join([str(k) for k in a]) for a in b]]
        return sorted([i for i in d if low <= i <= high])