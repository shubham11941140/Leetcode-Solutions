class Solution:

    def maxProfit(
        self,
        n: int,
        present: List[int],
        future: List[int],
        hierarchy: List[List[int]],
        budget: int,
    ) -> int:
        adj_list = defaultdict(list)
        for h in hierarchy:
            adj_list[h[0] - 1].append(h[1] - 1)

        @lru_cache(None)
        def dfs(employee, has_discount):
            cost = present[employee] // 2 if has_discount else present[employee]
            profit = future[employee] - cost

            buy_current = {cost: profit} if cost <= budget else {}
            skip_current = {0: 0}

            for child in adj_list[employee]:
                child_with_discount = dfs(child, True)  # Do something
                child_no_discount = dfs(child, False)  # Do nothing

                new_buy = {}
                for spent, prof in buy_current.items():
                    for child_spent, child_prof in child_with_discount.items():
                        ts = spent + child_spent
                        if ts <= budget:
                            tp = prof + child_prof
                            if ts not in new_buy or new_buy[ts] < tp:
                                new_buy[ts] = tp
                buy_current = new_buy
                new_skip = {}
                for spent, prof in skip_current.items():
                    for child_spent, child_prof in child_no_discount.items():
                        ts = spent + child_spent
                        if ts <= budget:
                            tp = prof + child_prof
                            if ts not in new_skip or new_skip[ts] < tp:
                                new_skip[ts] = tp
                skip_current = new_skip

            result = {}
            for spent, prof in buy_current.items():
                if spent not in result or result[spent] < prof:
                    result[spent] = prof
            for spent, prof in skip_current.items():
                if spent not in result or result[spent] < prof:
                    result[spent] = prof
            return result

        result = dfs(0, False)
        return max(result.values()) if result else 0
