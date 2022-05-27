class Solution:
    
    def rec(self, target, steps, double):
        if steps > self.ans:
            return
        if not double:
            self.rec(1, steps + target - 1, double)
        if target == 1:
            print(steps)
            self.ans = min(self.ans, steps)
            return
        elif target % 2:
            self.rec(target - 1, steps + 1, double)
        else:
            if double:
                self.rec(target // 2, steps + 1, double - 1)
            self.rec(target - 1, steps + 1, double)
            
    def moves(self, t, d):
        c = 0
        while d and t > 1:                
            c += 1
            if t % 2:
                t -= 1
            else:
                t //= 2
                d -= 1
            print(t, d, c)
        if t == 1:
            return c
        else:
            # t > 1 and d == 0
            return c + t - 1
            
            
        
    
    def minMoves(self, target: int, maxDoubles: int) -> int:
        # Rec solution
        return self.moves(target, maxDoubles)
        