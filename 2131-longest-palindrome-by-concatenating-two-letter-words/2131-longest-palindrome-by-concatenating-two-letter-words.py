class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = Counter(words)
        res = mid = 0 
        for i in d.keys():
            if i[0] == i[1]:
                res += d[i] if not d[i] % 2 else d[i] - 1
                mid |= d[i] % 2           
            elif i[::-1] in d:
                res += min(d[i], d[i[::-1]])
        return (res + mid) * 2        
