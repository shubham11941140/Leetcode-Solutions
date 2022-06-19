class Solution:
    
    def check(self, a, b, idx):
        return a[:idx + 1] == b[:idx + 1]
        
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Lex Sort
        products.sort()
        ans = []
        for idx, i in enumerate(searchWord):
            print(searchWord[:idx + 1])
            part = []
            l = 0
            for j in products:
                if self.check(searchWord, j, idx):
                    part.append(j)
                    l += 1
                    if l >= 3:
                        break
            print(part)
            ans.append(part)
        return ans
                    
        