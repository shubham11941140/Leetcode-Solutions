class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        d = {i: [] for i in range(n)}
        e = {i: 0 for i in range(n)}
        for i in meetings:
            f = False
            for j in d:
                # Unused case
                if not d[j]:
                    d[j].append(i)
                    e[j] = i[1]
                    f = True
                    break
                # If the meeting is not overlapping
                if i[0] >= d[j][-1][1] and e[j] <= i[0]:
                    # print(17, d[j], e[j], i)
                    d[j].append(i)
                    e[j] = i[1]
                    f = True
                    break
            if not f:
                m = min(e.values())
                # print(23, m)
                for j in d:
                    if e[j] == m:
                        e[j] = m + i[1] - i[0]
                        d[j].append(i)
                        break
        # print(d, e)
        f = {i: len(d[i]) for i in d}
        m = max(f.values())
        for i in f:
            if f[i] == m:
                return i
