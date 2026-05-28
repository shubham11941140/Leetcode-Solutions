class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:

        class Trie:
            def __init__(self):
                self.hs = {}
                self.best = (inf, inf)

            def search(self, word, head):
                prev = head
                for w in word:
                    if w in head.hs:
                        prev = head
                        head = head.hs[w]
                    else:
                        break

                return head.best[1]


            def build(self, word, head, ln, ind):
                
                for w in word:
                    head.best = min(head.best, (ln, ind))
                    if w in head.hs:
                        head = head.hs[w]
                    else:
                        tmp = Trie()
                        head.hs[w] = tmp
                        head = tmp

                head.best = min(head.best, (ln, ind))
                            
        head = Trie()
        
        for i in range(len(wordsContainer)):
            head.build(wordsContainer[i][::-1], head, len(wordsContainer[i]), i)

        return [head.search(j[::-1], head) for j in wordsQuery]      