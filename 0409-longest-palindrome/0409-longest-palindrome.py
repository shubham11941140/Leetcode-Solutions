class Solution:

    def longestPalindrome(self, s: str) -> int:
        char_freq = Counter(s)
        palindrome_length = 0
        for freq in char_freq.values():
            palindrome_length += freq // 2 * 2
            if palindrome_length % 2 == 0 and freq % 2 == 1:
                palindrome_length += 1
        return palindrome_length
