from sortedcontainers import SortedList


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.fc = {}
        self.fr = {}
        self.c = defaultdict(SortedList)
        for f, c, r in zip(foods, cuisines, ratings):
            self.fc[f] = c
            self.fr[f] = r
            self.c[c].add((-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        old_rating = self.fr[food]
        cuisine = self.fc[food]
        self.c[cuisine].remove((-old_rating, food))
        self.fr[food] = newRating
        self.c[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.c[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
