class Solution:

    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        previous_index = 0
        for index in spaces:
            result.append(s[previous_index:index])
            result.append(" ")
            previous_index = index
        result.append(s[previous_index:])
        return "".join(result)
