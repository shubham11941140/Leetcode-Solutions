class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:        
        people.sort(key = lambda x: (-x[0], x[1]))   
        a = []
        for i in people:
            a.insert(i[1], i)
        return a    
