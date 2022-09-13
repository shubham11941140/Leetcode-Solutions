class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        c = [bin(i).replace("0b", "").zfill(8) for i in data]     
        i = 0
        n = len(c)
        while i < n:
            s = c[i]
            flag = False
            # Check 4
            if i + 3 < n and s[:5] == "11110":
                if c[i + 1][:2] == "10" and c[i + 2][:2] == "10" and c[i + 3][:2] == "10":
                    flag = True
                    i += 3
                else:
                    return False
            # Check 3
            if i + 2 < n and s[:4] == "1110":
                if c[i + 1][:2] == "10" and c[i + 2][:2] == "10":
                    flag = True
                    i += 2
                else:
                    return False
            # Check 2
            if i + 1 < n and s[:3] == "110":
                if c[i + 1][:2] == "10":
                    flag = True
                    i += 1
                else:
                    return False                
            # Check 1            
            if s[:1] == "0":
                flag = True
            if not flag:
                return False
            i += 1
        return True
        