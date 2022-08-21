class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for i, item in enumerate(words):
            s = list(chars).copy()
            flag = True
            for j in item:                
                try:
                    s.remove(j)
                except:
                    flag = False
                    break
            if flag:
                ans += len(item)
        return ans
                 
        