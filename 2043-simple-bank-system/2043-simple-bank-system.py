class Bank:

    def __init__(self, balance: List[int]):
        self.b = balance   
        self.n = len(balance)     

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if max(account1, account2) > self.n or money > self.b[account1 - 1]:
            return False
        self.b[account1 - 1] -= money
        self.b[account2 - 1] += money     
        return True   

    def deposit(self, account: int, money: int) -> bool:
        if account > self.n:
            return False
        self.b[account - 1] += money
        return True
        
    def withdraw(self, account: int, money: int) -> bool:
        if account > self.n:
            return False
        if money > self.b[account - 1]:
            return False
        self.b[account - 1] -= money
        return True
        
# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)