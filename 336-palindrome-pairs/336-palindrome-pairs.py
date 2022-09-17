class Solution:

    def opt(self, w, n):
        return [[i, j] for i in range(n) for j in range(n)
                if i != j and (w[i] + w[j]) == (w[i] + w[j])[::-1]]

    def f(self, wordlist):
        hashmap_reverse = {
            word[::-1]: index
            for index, word in enumerate(wordlist)
        }
        ans = []
        for index, word in enumerate(wordlist):
            for i in range(len(word)):
                left, right = word[:i + 1], word[i + 1:]
                if (not len(left) == 0 and left == left[::-1]
                        and right in hashmap_reverse
                        and hashmap_reverse[right] != index):
                    ans.append([hashmap_reverse[right], index])

                # normal case.
                if (right == right[::-1] and left in hashmap_reverse
                        and hashmap_reverse[left] != index):
                    ans.append([index, hashmap_reverse[left]])
        return ans

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        return (self.opt(tuple(words), len(words))
                if len(words) <= 500 else self.f(words))
