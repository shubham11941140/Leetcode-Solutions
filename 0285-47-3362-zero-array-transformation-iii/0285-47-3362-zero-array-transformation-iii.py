class Solution:

    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort()  # Sort queries by starting index
        available = []  # Max heap for available `r` values
        running = []  # Min heap for running `r` values
        query_index = 0

        for i in range(len(nums)):
            while query_index < len(queries) and queries[query_index][0] <= i:
                heappush(
                    available, -queries[query_index][1]
                )  # Push negative for max heap
                query_index += 1

            while running and running[0] < i:
                heappop(running)

            while nums[i] > len(running):
                if not available or -available[0] < i:
                    return -1
                heappush(running, -heappop(available))

        return len(available)
