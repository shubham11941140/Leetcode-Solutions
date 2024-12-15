class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Function to calculate the improvement in pass ratio if an additional student is added
        def improvement(passed, total):
            return (passed + 1) / (total + 1) - passed / total
        # Initialize a max-heap with the negative improvement and the corresponding class data
        heap = [(-improvement(p, t), p, t) for p, t in classes]
        heapify(heap)
        # Distribute the extra students to maximize the overall pass ratio
        for _ in range(extraStudents):
            imp, p, t = heappop(heap)
            heappush(heap, (-improvement(p + 1, t + 1), p + 1, t + 1))
        # Calculate the final average pass ratio
        return sum(p / t for _, p, t in heap) / len(classes)