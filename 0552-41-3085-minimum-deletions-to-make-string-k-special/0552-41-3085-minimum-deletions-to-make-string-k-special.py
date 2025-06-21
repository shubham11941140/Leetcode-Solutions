class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = list(Counter(word).values())

        def deletions_for_threshold(threshold):
            deletions = 0
            for f in freq:
                if f < threshold:
                    deletions += f
                elif f > threshold + k:
                    deletions += f - threshold - k
            return deletions

        return min(deletions_for_threshold(t) for t in range(max(freq) + 1))        