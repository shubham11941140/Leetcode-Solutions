class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        print(c['b'])
        #for i in ['b', 'a', 'l', 'o', 'n']:
            #if i not in c:
                #return 0
        return min([c['b'], c['a'], c['l'] // 2, c['o'] // 2, c['n']])
        