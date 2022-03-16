class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        j = 0
        n = len(pushed)
        m = len(popped)
        while i < n or j < m:
            if stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            elif i == n and j < m:
                return False
            else:
                stack.append(pushed[i])
                i += 1
        return True
            
        