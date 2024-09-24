class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search_prefix_length(self, word):
        node = self.root
        length = 0
        for char in word:
            if char in node.children:
                node = node.children[char]
                length += 1
            else:
                break
        return length


class Solution:

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        for num in arr1:
            trie.insert(str(num))

        max_length = 0
        for num in arr2:
            max_length = max(max_length, trie.search_prefix_length(str(num)))

        return max_length
