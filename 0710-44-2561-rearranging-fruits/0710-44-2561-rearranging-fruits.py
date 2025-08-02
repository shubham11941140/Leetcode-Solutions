class Solution:

    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        total_counts = Counter(basket1) + Counter(basket2)

        for count in total_counts.values():
            if count % 2:
                return -1

        fruits_to_swap = []
        count1 = Counter(basket1)
        for fruit, total_count in total_counts.items():
            for _ in range(abs(count1.get(fruit, 0) - total_count // 2)):
                fruits_to_swap.append(fruit)

        fruits_to_swap.sort()

        min_val = min(total_counts.keys())
        return sum([
            min(fruits_to_swap[i], 2 * min_val)
            for i in range(len(fruits_to_swap) // 2)
        ])
