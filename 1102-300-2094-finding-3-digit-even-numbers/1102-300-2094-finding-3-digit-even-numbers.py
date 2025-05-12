class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = Counter(digits)
        res = []
        for i in range(1, 10):
            if freq[i] == 0: 
                continue
            freq[i] -= 1
            for j in range(10):
                if freq[j] == 0: 
                    continue
                freq[j] -= 1
                for k in range(0, 9, 2):
                    if freq[k] == 0: 
                        continue
                    res.append(i * 100 + j * 10 + k)
                freq[j] += 1
            freq[i] += 1
        return res        