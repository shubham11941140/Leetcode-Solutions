class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # count initial white blocks in the first window of size k
        count = blocks[:k].count('W')       
        # initialize the minimum recolors to the count in the first window
        min_recolors = count        
        # slide the window from left to right
        for i in range(1, len(blocks) - k + 1):
            if blocks[i - 1] == 'W':
                count -= 1
            if blocks[i + k - 1] == 'W':
                count += 1
            min_recolors = min(min_recolors, count)        
        return min_recolors    