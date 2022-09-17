# from cachetools import cached, TTLCache

# cache = TTLCache(maxsize=100, ttl=86400)


class Solution:

    # @cache(cache)
    def opt(self, w):
        n = len(w)
        ans = []
        for i in range(n):
            for j in range(i):
                k = w[i] + w[j]
                if k == k[::-1]:
                    ans.append([i, j])
            for j in range(i + 1, n):
                k = w[i] + w[j]
                if k == k[::-1]:
                    ans.append([i, j])
        return ans

    def f(self, wordlist):
        hashmap_reverse = {
            word[::-1]: index
            for index, word in enumerate(wordlist)
        }
        ans = []
        # enumerating over all words and for each character of them
        for index, word in enumerate(wordlist):
            for i in range(len(word)):
                # extracting left and right of them
                left, right = word[:i + 1], word[i + 1:]
                # checking if left exists and is palindrome and also right is present in map
                # this is to make sure the best edge case described holds.

                if (not len(left) == 0 and left == left[::-1]
                        and right in hashmap_reverse
                        and hashmap_reverse[right] != index):
                    ans.append([hashmap_reverse[right], index])

                # normal case.
                if (right == right[::-1] and left in hashmap_reverse
                        and hashmap_reverse[left] != index):
                    ans.append([index, hashmap_reverse[left]])
        # print(ans)
        return ans

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        if len(words) <= 500:
            w = tuple(words)
            return self.opt(w)
        return self.f(words)
