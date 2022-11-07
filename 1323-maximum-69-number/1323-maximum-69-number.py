class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str((num)))
        n = len(s)
        f = []
        for i in range(n):
            if s[i] == '6':
                t = s.copy()
                t[i] = '9'
                print(t)
                f.append(int(''.join(t)))
        print(f)
        return max(f) if f else num
                
        