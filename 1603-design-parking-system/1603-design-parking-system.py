class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.b = 0
        self.m = 0
        self.s = 0
        
    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.b < self.big:
            self.b += 1
            return True
        elif carType == 2 and self.m < self.medium:
            self.m += 1
            return True
        elif carType == 3 and self.s < self.small:
            self.s += 1
            return True                
        return False        

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)