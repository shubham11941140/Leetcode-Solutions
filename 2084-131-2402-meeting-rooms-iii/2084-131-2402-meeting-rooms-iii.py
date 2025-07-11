class Solution:

    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        d = {i: [] for i in range(n)}
        e = {i: 0 for i in range(n)}
        l = {i: 0 for i in range(n)}
        for i in meetings:
            f = False
            for j in d:
                # Unused case
                if not d[j]:
                    d[j] = i
                    l[j] += 1
                    e[j] = i[1]
                    f = True
                    break
                # If the meeting is not overlapping
                if i[0] >= d[j][1] and e[j] <= i[0]:
                    d[j] = i
                    e[j] = i[1]
                    l[j] += 1
                    f = True
                    break
            if not f:
                m = min(e.values())
                for j in d:
                    if e[j] == m:
                        e[j] += i[1] - i[0]
                        d[j] = i
                        l[j] += 1
                        break
        m = max(l.values())
        return [i for i in l if l[i] == m][0]
