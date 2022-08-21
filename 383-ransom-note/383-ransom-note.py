class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        try:
            for i in ransomNote:
                magazine.remove(i)
            return True
        except:
            return False
            pass
