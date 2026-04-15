class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_distance = float('inf')
        if target not in words:
            return -1

        return min([min((i - startIndex + n) % n, (startIndex - i + n) % n) for i, word in enumerate(words) if word == target])

        return -1 if min_distance == float('inf') else min_distance        