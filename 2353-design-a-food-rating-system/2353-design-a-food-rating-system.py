import collections
import itertools

from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.fc = {}
        self.fr = {}
        self.__cusine_to_rating_foods = collections.defaultdict(SortedList)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.fc[food] = cuisine
            self.fr[food] = rating
            self.__cusine_to_rating_foods[cuisine].add((-rating, food))        

    def changeRating(self, food: str, newRating: int) -> None:
        old_rating = self.fr[food]
        cuisine = self.fc[food]
        self.__cusine_to_rating_foods[cuisine].remove((-old_rating, food))
        self.fr[food] = newRating
        self.__cusine_to_rating_foods[cuisine].add((-newRating, food))        

    def highestRated(self, cuisine: str) -> str:
        return self.__cusine_to_rating_foods[cuisine][0][1]        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)