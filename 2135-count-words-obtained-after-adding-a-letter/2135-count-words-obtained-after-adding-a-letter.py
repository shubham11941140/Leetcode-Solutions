class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        b = set()
        for i in startWords:
            a = [chr(j) for j in range(97, 123) if chr(j) not in i]
            for k in a:
                b.add(''.join(sorted(i + k)))
        return sum(1 for i in targetWords if ''.join(sorted(i)) in b)