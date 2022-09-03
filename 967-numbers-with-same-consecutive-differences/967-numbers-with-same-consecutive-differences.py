class Solution:
    
    
    def rec(self, n, k, a, ans):
        if len(a) == n:
            s = ''.join([str(x) for x in a])
            ans.append(int(s))
            return
        print(a)
        prev = a[-1]
        possible = [prev + k, prev - k]
        for i in possible:
            if 0 <= i <= 9:
                # Append i to a and recurse
                self.rec(n, k, a + [i], ans)
    
    
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # Recursion solution
        ans = []
        for i in range(1, 10):
            self.rec(n, k, [i], ans)
        print(ans)
        return list(set(ans))
                    