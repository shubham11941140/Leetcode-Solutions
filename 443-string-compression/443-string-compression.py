from copy import deepcopy

class Solution:
    def compress(self, chars: List[str]) -> int:
        #generate
        a = []
        n = len(chars)
        print(type(chars))
        print(type(chars[0]))
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
        print(a)
        b = []
        for i, j in a:
            b.append(i)
            if j > 1:
                b += list(str(j))
        print(b)
        for i in range(len(b)):
            chars[i] = b[i]
        while len(chars) > len(b):
            chars.pop()
        return len(chars)
        chars.clear()
        print(chars)
        chars = b.copy()
        return chars
        chars = deepcopy(b)
        print(chars, len(chars))
        #print(type(chars[0]))
        #print(len(chars))
        return [str(i) for i in chars]
                
        