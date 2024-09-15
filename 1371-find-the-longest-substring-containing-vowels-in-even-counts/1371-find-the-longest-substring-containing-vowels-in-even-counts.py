class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        state_to_index = {0: -1}
        vowels = "aeiou"
        state = 0
        max_length = 0

        for i, char in enumerate(s):
            if char in vowels:
                # Toggle the bit corresponding to the vowel
                state ^= 1 << vowels.index(char)

            if state in state_to_index:
                # Calculate the length of the substring
                max_length = max(max_length, i - state_to_index[state])
            else:
                # Store the first occurrence of this state
                state_to_index[state] = i

        return max_length
