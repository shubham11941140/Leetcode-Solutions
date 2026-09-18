class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.mp = {}  # taskId -> (userId, priority)
        self.st = []  # sorted list of (priority, taskId)

        for userId, taskId, priority in tasks:
            self.mp[taskId] = (userId, priority)
            insort(self.st, (priority, taskId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.mp[taskId] = (userId, priority)
        insort(self.st, (priority, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, oldPriority = self.mp[taskId]
        idx = bisect_left(self.st, (oldPriority, taskId))
        self.st.pop(idx)
        self.mp[taskId] = (userId, newPriority)
        insort(self.st, (newPriority, taskId))

    def rmv(self, taskId: int) -> None:
        userId, priority = self.mp[taskId]
        idx = bisect_left(self.st, (priority, taskId))
        self.st.pop(idx)
        del self.mp[taskId]

    def execTop(self) -> int:
        if not self.mp:
            return -1
        priority, taskId = self.st.pop()  # highest priority
        userId, _ = self.mp[taskId]
        del self.mp[taskId]
        return userId


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
