class Solution:

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Initialize a max-heap with the negative improvement and the corresponding class data
        heap = [(-((p + 1) / (t + 1) - (p / t)), p, t) for p, t in classes]
        heapify(heap)
        # Distribute the extra students to maximize the overall pass ratio
        for _ in range(extraStudents):
            imp, p, t = heappop(heap)
            heappush(heap, (-((p + 2) / (t + 2) - (p + 1) / (t + 1)), p + 1, t + 1))
        # Calculate the final average pass ratio
        return sum(p / t for _, p, t in heap) / len(classes)
