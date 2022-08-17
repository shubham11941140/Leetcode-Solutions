class ATM:

    def __init__(self):
        self.a = [0] * 5
        self.b = [20, 50, 100, 200, 500]
        

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.a[i] += banknotesCount[i]
        

    def withdraw(self, amount: int) -> List[int]:
        # Greedy
        f = self.a.copy()
        ans = [0] * 5
        for i in reversed(range(5)):
                r = amount % self.b[i]
                q = amount // self.b[i]
                if self.a[i] >= q:
                    amount -= (q * self.b[i])
                    ans[i] = q
                    self.a[i] -= q
                else:
                    amount -= (self.a[i] * self.b[i])
                    ans[i] = self.a[i]
                    self.a[i] = 0
                if not amount:
                    break
        if amount:
            for i in range(5):
                self.a[i] += ans[i]
            return [-1] 
        print(f, self.a, ans)
        return ans
            
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)