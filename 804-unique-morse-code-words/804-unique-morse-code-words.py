class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans = []
        for i in words:
            s = ""
            for j in i:
                k = ord(j) - ord('a')
                s += m[k]
            ans.append(s)
        return len(set(ans))
        