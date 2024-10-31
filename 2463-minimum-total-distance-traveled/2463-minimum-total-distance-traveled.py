class Solution:

    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        fp = [f[0] for f in factory]
        factory_limits = [f[1] for f in factory]

        # Memoized recursive function
        @lru_cache(None)
        def dp(robot_idx: int, factory_idx: int) -> int:
            if robot_idx == len(robot):
                return 0
            # If we run out of factories, return an arbitrarily large number (infeasible path)
            if factory_idx == len(fp):
                return float("inf")
            min_distance = dp(robot_idx, factory_idx + 1)

            # Option 2: Assign robots to this factory up to its limit
            total_distance = 0
            for i in range(factory_limits[factory_idx]):
                if robot_idx + i < len(robot):
                    total_distance += abs(robot[robot_idx + i] - fp[factory_idx])
                    min_distance = min(
                        min_distance,
                        total_distance + dp(robot_idx + i + 1, factory_idx + 1),
                    )
                else:
                    break
            return min_distance

        return dp(0, 0)
