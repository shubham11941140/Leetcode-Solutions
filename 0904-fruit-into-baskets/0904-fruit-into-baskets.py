class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        max_fruits = 0
        start = 0
        for end in range(len(fruits)):
            if fruits[end] not in basket:
                basket[fruits[end]] = 0
            basket[fruits[end]] += 1
            while len(basket) > 2:
                basket[fruits[start]] -= 1
                if basket[fruits[start]] == 0:
                    del basket[fruits[start]]
                start += 1
            max_fruits = max(max_fruits, end - start + 1)
        return max_fruits
