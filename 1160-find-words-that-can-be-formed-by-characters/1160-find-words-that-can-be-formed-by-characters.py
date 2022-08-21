class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for i in range(len(words)):
            s = list(chars).copy()
            flag = True
            for j in words[i]:
                try:
                    s.remove(j)
                except:
                    flag = False
                    break
            if flag:
                ans += len(words[i])
        return ans
