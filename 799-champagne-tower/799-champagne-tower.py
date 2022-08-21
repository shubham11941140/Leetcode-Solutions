from collections import Counter


class Solution:

    def champagneTower(self, poured: int, query_row: int,
                       query_glass: int) -> float:
        # print(inorder)

        # Store all child in an array

        # Apply dp

        if not poured:
            return 0
        c = [[0 for i in range(101)] for j in range(101)]
        c[0][0] = poured
        for r in range(query_row + 1):
            for col in range(r + 1):
                left = (c[r][col] - 1) / 2
                if left > 0:
                    c[r + 1][col] += left
                    c[r + 1][col + 1] += left
        return min(1, c[query_row][query_glass])

        ca = [[] for i in range(110)]
        c = [0]
        ca[1].append(0)
        c.append(Counter(ca[1]))
        for i in range(2, 101):
            b = ca[i - 1]
            for j in b:
                ca[i].append(j - 1)
                ca[i].append(j + 1)
            c.append(Counter(ca[i]))
            ca[i] = sorted(list(set(ca[i])))
        # Allocate glasses in ca
        # for i in ca:            print(*i)
        print(23)
        p = poured
        d = [0]
        for i in range(1, 101):
            if p == 0:
                break
            if p < i:
                # Freq allocation
                print(31)
                print(p, i)
                print(c[i])
                s = sum(c[i].values())

                break
            if p >= i:
                p -= i
                z = []
                for j in ca[i]:
                    z.append((j, 1))
                d.append(z)
        print(d)
