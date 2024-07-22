class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        p = sorted([(heights[i], names[i]) for i in range(n)], reverse = True)
        return [y for x, y in p]
        
        
        