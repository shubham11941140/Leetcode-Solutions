class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        a = [(idxi + idxj, i) for idxi, i in enumerate(list1) for idxj, j in enumerate(list2) if i == j]
        m = min([x for x, y in a])
        return [y for x, y in a if x == m]
        
        