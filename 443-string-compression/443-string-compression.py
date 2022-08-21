class Solution:
    def compress(self, chars: List[str]) -> int:
        a = []
        n = len(chars)
        i = 0
        
        while i < n:
            j = chars[i]
            c = 0
            while j == chars[i] and i < n:
                c += 1
                i += 1
                if i == n:
                    break
            a.append((j, c))
            
        b = []
        for i, j in a:
            b.append(i)
            if j > 1:
                b += list(str(j))
                
        for i, item in enumerate(b):
            chars[i] = item
            
        while len(chars) > len(b):
            chars.pop()
            
        return len(chars)
                
        