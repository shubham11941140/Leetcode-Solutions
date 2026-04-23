class Solution:

    def interpret(self, command: str) -> str:
        s = command
        s = s.replace("(al)", "al")
        s = s.replace("()", "o")
        return s
