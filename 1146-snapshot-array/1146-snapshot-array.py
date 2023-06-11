class SnapshotArray:

    def __init__(self, length: int):
        self.l = length
        self.a = [0 for i in range(length)]
        self.s = 0
        self.d = defaultdict(dict)
        self.snap_id = 0
        self.array = [[[-1, 0]] for _ in range(length)]        

    def set(self, index: int, val: int) -> None:
        #self.d[self.s][index] = val
        #self.a[index] = val
        if self.array[index][-1][0] == self.snap_id:
            self.array[index][-1][1] = val
        else:
            self.array[index].append([self.snap_id, val])
        
        

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1        
        self.s += 1
        #self.d[self.s] = self.a.copy()
        self.d[self.s] = self.d[self.s - 1].copy()
        return self.s - 1     
    

    def get(self, index: int, snap_id: int) -> int:
        
        i = bisect.bisect(self.array[index], [snap_id + 1]) - 1
        return self.array[index][i][1]        
        
        
        #print(snap_id, self.d[snap_id])
        if not self.d[snap_id]:
            return 0
        if index not in self.d[snap_id]:
            return 0
        return self.d[snap_id][index] 
    
        
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

    def __init__(self, length):
        self.snap_id = 0
        self.array = [[[-1, 0]] for _ in range(length)]

    def set(self, index, val):
        if self.array[index][-1][0] == self.snap_id:
            self.array[index][-1][1] = val
        else:
            self.array[index].append([self.snap_id, val])

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        i = bisect.bisect(self.array[index], [snap_id + 1]) - 1
        return self.array[index][i][1]