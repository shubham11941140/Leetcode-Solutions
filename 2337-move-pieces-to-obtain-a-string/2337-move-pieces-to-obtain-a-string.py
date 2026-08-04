class Solution:

    def canChange(self, start: str, target: str) -> bool:
        s = [ch for ch in start if ch != "_"]
        t = [ch for ch in target if ch != "_"]
        if s != t:
            return False
        # Check L's positions
        j = 0
        for i in range(len(start)):
            if start[i] == "L":
                while target[j] != "L":
                    j += 1
                if i < j:
                    return False
                j += 1
        # Check R's positions
        j = 0
        for i in range(len(start)):
            if start[i] == "R":
                while target[j] != "R":
                    j += 1
                if i > j:
                    return False
                j += 1
        return True
