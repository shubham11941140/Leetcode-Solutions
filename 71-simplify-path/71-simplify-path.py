class Solution:
    def simplifyPath(self, path: str) -> str:
        while '/./' in path:
            path = path.replace('/./', '/')
        print(path)
        i = 0   
        path += '/'
        n = len(path)
        stack = []
        curr = []
        print(path)
        while i < n:            
            if path[i] == '/':
                if curr:
                    if ''.join(curr) == '..': 
                        if stack:
                            stack.pop()
                    elif ''.join(curr) == '.':
                        # Do nothing
                        m = 1
                    else:
                        stack.append(curr)
                    curr = []
            else:                
                curr.append(path[i])
            i += 1
            
          
        print(curr)
        print(stack)
        if curr:
            stack.append(curr)
        s = ""
        for k in stack:
            s += ('/' + ''.join(k))
        if s == "":
            return "/"
        return s
            
                
            
            
        
        
        