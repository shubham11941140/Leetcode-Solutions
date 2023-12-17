import collections
import itertools

from sortedcontainers import SortedList


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        self.__food_to_cuisine = {}
        self.__food_to_rating = {}
        self.__cusine_to_rating_foods = collections.defaultdict(SortedList)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.__food_to_cuisine[food] = cuisine
            self.__food_to_rating[food] = rating
            self.__cusine_to_rating_foods[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        old_rating = self.__food_to_rating[food]
        cuisine = self.__food_to_cuisine[food]
        self.__cusine_to_rating_foods[cuisine].remove((-old_rating, food))
        self.__food_to_rating[food] = newRating
        self.__cusine_to_rating_foods[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        """
        :type cuisine: str
        :rtype: str
        """
        return self.__cusine_to_rating_foods[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
