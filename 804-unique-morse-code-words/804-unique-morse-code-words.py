class Solution:

    @staticmethod
    def uniqueMorseRepresentations(words: List[str]) -> int:
        m = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        return len({"".join([m[ord(j) - ord("a")] for j in i]) for i in words})
