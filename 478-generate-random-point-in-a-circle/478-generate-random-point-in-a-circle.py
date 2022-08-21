from random import uniform

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center  
    
    def generate(self):
        x = uniform(self.x - self.r, self.x + self.r)
        y = uniform(self.y - self.r, self.y + self.r)
        return (x, y)
    
    def equation(self, x, y):
        return (x - self.x) ** 2 + (y - self.y) ** 2 <= self.r ** 2
        
    def randPoint(self) -> List[float]:
        while True:
            x, y = self.generate()
            if self.equation(x, y):
                return [x, y]        

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
