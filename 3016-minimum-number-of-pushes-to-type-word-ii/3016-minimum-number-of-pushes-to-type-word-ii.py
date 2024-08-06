class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count the frequency of each letter in the word
        freq = Counter(word)
        
        # Sort the frequencies in descending order
        sorted_freq = sorted(freq.values(), reverse=True)
        
        total_presses = 0
        for i, count in enumerate(sorted_freq):
            # Calculate the number of presses for each letter
            presses = (i // 8) + 1
            total_presses += presses * count
        
        return total_presses        