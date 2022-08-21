class Solution:

    @staticmethod
    def simplifyPath(path: str) -> str:
        path += "/"
        n = len(path)
        stack = []
        curr = []
        for i in range(n):
            if path[i] == "/":
                if curr:
                    if "".join(curr) == "..":
                        if stack:
                            stack.pop()
                    elif "".join(curr) == ".":
                        # Do nothing
                        m = 1
                    else:
                        stack.append(curr)
                    curr = []
            else:
                curr.append(path[i])
        if curr:
            stack.append(curr)
        s = "".join([("/" + "".join(k)) for k in stack])
        if s == "":
            return "/"
        return s
