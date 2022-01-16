class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        a = [i for i in range(len(seats)) if seats[i]]
        print(a)
        d = []
        
        # diff in points
        for i in range(1, len(a)):
            b = a[i] - a[i - 1]
            c = (b) // 2
            d.append(c)
        print(d)
        d.append(len(seats) - 1 - a[-1])
        d.append(a[0])
        return max(d)
        print()
        print(a[0] - 0)
        return 1
        # 2 pointer to check min absolute diff
        j = 0
        i = 0
        while i < n:
            if a[i] == j:
                i += 1
                j += 1
            elif a[i] < j:
                i += 1
            elif a[i] > j:
                j += 1
        
        