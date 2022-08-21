class Solution:

    def titleToNumber(self, columnTitle: str) -> int:
        return (sum([(26**i) for i in range(1, len(columnTitle))]) + sum(
            [(ord(columnTitle[i]) - ord("A")) * pow(26,
                                                    len(columnTitle) - i - 1)
             for i in range(len(columnTitle))]) + 1)
