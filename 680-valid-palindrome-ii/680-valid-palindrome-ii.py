class Solution:
    
    def pal(self, s):
        l = 0
        r = len(s) - 1
        # print(s)
        while l <= r:
            # print(8, l, r)
            if s[l] == s[r]:
                l += 1
                r -= 1            
            else:
                return False
        return True
    
    def palli(self, s):
        return s == s[::-1]

    def validPalindrome(self, s: str) -> bool:
        if self.palli(s):
            return True
        
        if len(s) <= 1000:
            for i in range(len(s)):
                t = s[:i] + s[i + 1:]
                # print(t)
                if self.palli(t):
                    return True
            return False        
        
        l = 0
        r = len(s) - 1
        while l <= r:
            print(l, r)
            if l == r:
                return True
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif s[l] != s[r]:
                # Conflict at 2 indexes
                
                # Increment and check
                # Decrement and check
                print(45, l, r)
                L = s[:l] + s[l + 1:]
                R = s[:r] + s[r + 1:]
                if self.palli(L) or self.palli(R):
                    return True
                break
                #print("L", s[:l], s[l + 1:])
                #print("R", s[:r], s[r + 1:])
                # break
                
                '''
                
                left = l
                right = r
                l += 1
                while l <= r:
                    if l == r:
                        return True                    
                    if s[l] == s[r]:
                        l += 1
                        r -= 1
                    else:
                        break
                
                right -= 1
                while left <= right:
                    if left == right:
                        return True
                    if s[left] == s[right]:
                        left += 1
                        right -= 1
                    else:
                        break
                '''
        return False
             
        
        '''
        for i in range(len(s)):
            t = s[:i] + s[i + 1:]
            if self.pal(t):
                return True
        return False
        '''
    
        