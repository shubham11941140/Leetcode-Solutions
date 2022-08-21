class Solution:

    @staticmethod
    def suggestedProducts(products: List[str],
                          searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        for idx, i in enumerate(searchWord):
            part = []
            l = 0
            for j in products:
                if searchWord[:idx + 1] == j[:idx + 1]:
                    part.append(j)
                    l += 1
                    if l >= 3:
                        break
            ans.append(part)
        return ans
