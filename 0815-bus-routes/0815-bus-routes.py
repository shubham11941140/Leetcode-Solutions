class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source == target:
            return 0

        stops_to_routes = defaultdict(set)
        for route_id, stops in enumerate(routes):
            for stop in stops:
                stops_to_routes[stop].add(route_id)

        graph = defaultdict(set)
        for stop, route_ids in stops_to_routes.items():
            for route_id in route_ids:
                graph[route_id].update(route_ids)

        routes = [set(route) for route in routes]
        initial_routes = list(stops_to_routes[source])
        q = deque(initial_routes)
        num_stops = 0
        seen_routes = set(initial_routes)

        while q:
            size = len(q)
            num_stops += 1
            for _ in range(size):
                route_id = q.popleft()
                if target in routes[route_id]:
                    return num_stops
                for next_route_id in graph[route_id]:
                    if next_route_id not in seen_routes:
                        q.append(next_route_id)
                        seen_routes.add(next_route_id)
        return -1
        