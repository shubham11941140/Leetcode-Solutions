class Solution:

    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        workers = sorted([float(w) / q, q] for w, q in zip(wage, quality))
        res = float("inf")
        qsum = 0
        queue = []
        for r, q in workers:
            heappush(queue, -q)
            qsum += q
            if len(queue) > k:
                qsum += heappop(queue)
            if len(queue) == k:
                res = min(res, qsum * r)
        return res
