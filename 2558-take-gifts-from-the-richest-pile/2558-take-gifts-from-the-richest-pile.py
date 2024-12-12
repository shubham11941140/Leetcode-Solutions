class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        piles = gifts
        max_heap = [-pile for pile in piles]
        heapq.heapify(max_heap)

        for _ in range(k):
            # Take the largest pile, revert its sign back to positive
            largest_pile = -heapq.heappop(max_heap)

            # Take gifts from the richest pile (the problem statement should specify how many gifts to take)
            # For demonstration, let's assume we take half of the largest pile each time
            gifts_taken = largest_pile // 2

            # Remaining gifts in the largest pile
            remaining_gifts = floor(sqrt(largest_pile))

            # Push the remaining gifts back to the heap (as a negative value)
            heapq.heappush(max_heap, -remaining_gifts)

        # Convert the max-heap back to a list of positive values
        final_piles = [-heapq.heappop(max_heap) for _ in range(len(max_heap))]
        final_piles.sort(reverse=True)

        print(final_piles)
        return sum(final_piles)