class Solution:

    def opt(self, w, n):
        return [[i, j] for i in range(n) for j in range(n)
                if i != j and (w[i] + w[j]) == (w[i] + w[j])[::-1]]

    def f(self, wordlist, n):
        h = {wordlist[i][::-1]: i for i in range(n)}
        ans = []
        for index, word in enumerate(wordlist):
            for i in range(len(word)):
                left, right = word[:i + 1], word[i + 1:]
                if left and left == left[::-1] and right in h and h[
                        right] != index:
                    ans.append([h[right], index])
                if right == right[::-1] and left in h and h[left] != index:
                    ans.append([index, h[left]])
        return ans

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        return (self.opt(tuple(words), len(words))
                if len(words) <= 30 else self.f(words, len(words)))
