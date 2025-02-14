class ProductOfNumbers:

    def __init__(self):
        self.p = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # Reset the list if zero is added
            self.p = [1]
        else:
            # Append the new product to the list
            self.p.append(self.p[-1] * num)        

    def getProduct(self, k: int) -> int:
        return 0 if k >= len(self.p) else self.p[-1] // self.p[-1 - k]  

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)