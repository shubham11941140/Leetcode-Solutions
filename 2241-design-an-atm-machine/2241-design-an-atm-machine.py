class ATM:

    def __init__(self):
        self.a = [0] * 5
        self.b = [20, 50, 100, 200, 500]
        
    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.a[i] += banknotesCount[i]
        
    def withdraw(self, amount: int) -> List[int]:
        ans = [0] * 5
        for i in reversed(range(5)):
            m = min((amount // self.b[i]), self.a[i])
            amount -= (m * self.b[i])
            ans[i] = m
            self.a[i] -= m
            if not amount:
                break
        if amount:
            for i in range(5):
                self.a[i] += ans[i]
            return [-1] 
        return ans
            
# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
