class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(set(arr))
        rank_dict = {num: rank + 1 for rank, num in enumerate(sorted_unique)}
        return [rank_dict[num] for num in arr]        