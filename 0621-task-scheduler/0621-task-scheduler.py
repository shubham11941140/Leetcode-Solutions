class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = list(Counter(tasks).values())
        max_count = max(task_counts)
        max_count_tasks = task_counts.count(max_count)
        return max(len(tasks), (max_count - 1) * (n + 1) + max_count_tasks)        