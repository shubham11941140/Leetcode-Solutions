class Solution:
    def compress(self, chars: List[str]) -> int:
        a = []
        n = len(chars)
        i = 0
        while i < n:
            cc = chars[i]
            count = 0
            while cc == chars[i]:
                count += 1
                i += 1
                if i == n:
                    break
            a.append([cc, count])
        chars.clear()
        for i in a:
            chars.append(i[0])
            if i[1] > 1:
                for j in str(i[1]):
                    chars.append(j)
        return len(chars)       