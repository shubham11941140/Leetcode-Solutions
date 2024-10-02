class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank_dict = {num: rank + 1 for rank, num in enumerate(sorted(set(arr)))}
        return [rank_dict[i] for i in arr]        