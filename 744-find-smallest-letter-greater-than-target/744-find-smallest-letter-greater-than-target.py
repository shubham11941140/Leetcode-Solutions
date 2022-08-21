class Solution:

    @staticmethod
    def nextGreatestLetter(letters: List[str], target: str) -> str:
        for i, item in enumerate(letters):
            if ord(item) > ord(target):
                return item
        return letters[0]
