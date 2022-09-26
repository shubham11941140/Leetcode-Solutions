class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        @cache
        def dfs(i, curr, prev, string):
            if i == len(num):
                if curr == target:
                    res.append(string)
                return
            for j in range(i, len(num)):
                if j != i and num[i] == '0':
                    break
                curr_num = int(num[i:j + 1])
                if i == 0:
                    dfs(j + 1, curr_num, curr_num, string + str(curr_num))
                else:
                    dfs(j + 1, curr + curr_num, curr_num, string + '+' + str(curr_num))
                    dfs(j + 1, curr - curr_num, -curr_num, string + '-' + str(curr_num))
                    dfs(j + 1, curr - prev + prev * curr_num, prev * curr_num, string + '*' + str(curr_num))
        res = []
        dfs(0, 0, 0, '')
        return res        