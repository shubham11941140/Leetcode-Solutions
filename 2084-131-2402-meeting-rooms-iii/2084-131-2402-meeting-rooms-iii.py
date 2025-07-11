class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available = list(range(n))
        heapify(available)

        busy = []  # (end_time, room_id)
        count = [0] * n

        for start, end in sorted(meetings):
            while busy and busy[0][0] <= start:
                _, room = heappop(busy)
                heappush(available, room)

            if available:
                room = heappop(available)
                heappush(busy, (end, room))
            else:
                end_time, room = heappop(busy)
                heappush(busy, (end_time + (end - start), room))

            count[room] += 1

        return count.index(max(count))