class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        #print(list(enumerate(list1)))
        a = []
        for idxi, i in list(enumerate(list1)):
            for idxj, j in list(enumerate(list2)):
                if i == j:
                    a.append((idxi + idxj, i))
        #print(a)
        m = min([x for x, y in a])
        ans = []
        for x, y in a:
            if x == m:
                ans.append(y)
        return ans
        
        