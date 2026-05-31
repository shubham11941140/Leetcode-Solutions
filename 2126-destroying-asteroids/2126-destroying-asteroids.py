class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        for i in sorted(asteroids):
            if mass >= i:
                mass += i
            else:
                return False
        return True        