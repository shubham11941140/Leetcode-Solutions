class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        ans = [-1] * n
        st = []
        for i in reversed(range(n)):
            pos, speed = cars[i]
            while st and speed <= cars[st[-1]][1]:
                st.pop()
            while st:
                j = st[-1]
                r = (cars[j][0] - pos) / (speed - cars[j][1])
                if r <= ans[j] or ans[j] == -1:
                    ans[i] = r
                    break
                st.pop()
            st.append(i)
        return ans       