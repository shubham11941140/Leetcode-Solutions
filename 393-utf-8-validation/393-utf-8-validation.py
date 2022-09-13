class Solution:

    def validUtf8(self, data: List[int]) -> bool:
        c = [bin(i).replace("0b", "").zfill(8) for i in data]
        i = 0
        n = len(c)
        while i < n:
            flag = False
            if i + 3 < n and c[i][:5] == "11110":
                if (c[i + 1][:2] == "10" and c[i + 2][:2] == "10"
                        and c[i + 3][:2] == "10"):
                    flag = True
                    i += 3
                else:
                    return False
            if i + 2 < n and c[i][:4] == "1110":
                if c[i + 1][:2] == "10" and c[i + 2][:2] == "10":
                    flag = True
                    i += 2
                else:
                    return False
            if i + 1 < n and c[i][:3] == "110":
                if c[i + 1][:2] == "10":
                    flag = True
                    i += 1
                else:
                    return False
            if c[i][0] == "0":
                flag = True
            if not flag:
                return False
            i += 1
        return True
