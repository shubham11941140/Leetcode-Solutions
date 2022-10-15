class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        b = []
        for i in startWords:
            # List all characters from a-z not in i
            a = [chr(j) for j in range(97, 123) if chr(j) not in i]
            for k in a:
                b.append(''.join(sorted(i + k)))
        sb = set(b)
        return sum(1 for i in targetWords if ''.join(sorted(i)) in sb)