class Solution:

    def validUtf8(self, data: List[int]) -> bool:
        c = [bin(i).replace("0b", "").zfill(8) for i in data]
        # c = [i.zfill(8) for i in b]
        i = 0
        n = len(c)
        while i < n:
            s = c[i]
            flag = False
            # Check 4
            if i + 3 < n and s[:5] == "11110":
                if (len([
                        1 for y in [c[i + 1], c[i + 2], c[i + 3]]
                        if y[:2] == "10"
                ]) == 3):
                    flag = True
                    i += 3
                else:
                    return False
            # Check 3
            if i + 2 < n and s[:4] == "1110":
                if len([1 for y in [c[i + 1], c[i + 2]]
                        if y[:2] == "10"]) == 2:
                    flag = True
                    i += 2
                else:
                    return False
            # Check 2
            if i + 1 < n and s[:3] == "110":
                if len([1 for y in [c[i + 1]] if y[:2] == "10"]) == 1:
                    flag = True
                    i += 1
                else:
                    return False
            # Check 1
            if s[:1] == "0":
                flag = True
                i += 0
            if not flag:
                return False
            i += 1
        return True
