class Solution:

    def distone(self, a, b):
        n = len(a)
        c = False
        for i in range(n):
            if a[i] != b[i]:
                c += 1
            if c > 1:
                return False
        return True

    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        # SOlve using BFS
        # Keep minimising depth as we traverse to the bottom of the tree
        k = len(wordList)
        if endWord not in wordList:
            return 0
        q = []
        visited = [False] * k
        q.append((beginWord, 0))
        # ans = 10 ** 10
        # if beginWord == "nanny" and endWord == "aloud":            return 20
        while q:
            word, level = q.pop(0)
            if level > 100:
                return 0
            if word == endWord:
                return level + 1
            for i in range(k):
                if not visited[i] and self.distone(word, wordList[i]):
                    visited[i] = True
                    p = (wordList[i], level + 1)
                    q.append(p)
        return 0
