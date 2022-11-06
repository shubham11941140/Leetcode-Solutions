class Solution:

    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        ans = [-1] * n
        st = []
        for i in range(n - 1, -1, -1):
            pos, speed = cars[i]
            while st and speed <= cars[st[-1]][1]:
                st.pop()
            while st:
                j = st[-1]
                if (cars[j][0] - pos) / (speed -
                                         cars[j][1]) <= ans[j] or ans[j] == -1:
                    ans[i] = (cars[j][0] - pos) / (speed - cars[j][1])
                    break
                st.pop()
            st.append(i)
        return ans
