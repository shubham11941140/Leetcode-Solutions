class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        items.sort(key=lambda x: x[1])
        minPrice = items[0][1]
        factorCount = [0] * (n + 1)
        for i in range(n):
            factorCount[items[i][0]] += 1

        freeCount = [0] * (n + 1)
        for f in range(1, n + 1):
            if factorCount[f]:
                for multiple in range(f, n + 1, f):
                    freeCount[f] += factorCount[multiple]

        copies = [0] * n
        for i in range(n):
            copies[i] = freeCount[items[i][0]] - 1

        remainBudget = budget
        totalItems = 0
        for i in range(n):
            price = items[i][1]
            if price >= 2 * minPrice or price > remainBudget:
                break
            if not copies[i]:
                continue
            take = min(copies[i], remainBudget // price)
            totalItems += 2 * take
            remainBudget -= take * price

        return totalItems + remainBudget // minPrice