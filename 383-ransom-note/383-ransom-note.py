class Solution:

    @staticmethod
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        try:
            for i in ransomNote:
                magazine.remove(i)
            return True
        except:
            return False
