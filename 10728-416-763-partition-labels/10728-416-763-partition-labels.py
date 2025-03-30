class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Track the last occurrence of each character
        last_occurrence = {char: idx for idx, char in enumerate(s)}        
        partitions = []
        start, end = 0, 0        
        for idx, char in enumerate(s):
            # Extend the current partition's end to the farthest last occurrence
            end = max(end, last_occurrence[char])            
            if idx == end:
                # Once the current index matches the partition's end, add it to the result
                partitions.append(end - start + 1)
                start = idx + 1        
        return partitions      