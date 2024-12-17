class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        arr = [0] * 26
        a = ord('a')        
        for char in s:
            arr[ord(char)-a] += 1			
        # Using an array to store the answer as appending to a string is a costly operation
        ans = []
        curr = 25
        prev = 24 		
        # We are starting with curr = 25 as we need to add the largest character first
        while curr >= 0:
            if arr[curr] == 0:
                curr -= 1
                continue 
            for i in range(min(repeatLimit, arr[curr])):
                ans.append(chr(curr + a))
                arr[curr] -= 1
            if arr[curr] == 0:
                curr -= 1
                continue
            g = False
            for j in range(min(prev, curr-1), -1, -1):
                if arr[j]:
                    g = True
                    arr[j] -= 1
                    prev = j
                    ans.append(chr(j + a))
                    break
            if not g: 
                break        
        return ''.join(ans)     