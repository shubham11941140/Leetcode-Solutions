class Solution:   
        
    def maxArea(self, height: List[int]) -> int:
        # Find farthest greater element on left and right
        l = 0
        r = len(height) - 1
        ans = -1
        while l <= r:
            area = (r - l) * min(height[l], height[r])
            ans = max(ans, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans
        
        
        n = len(height)
        rh = self.far_great_right(height, n)
        lh = self.far_great_left(height, n)
        '''
        rh = [-1] * n
        lh = [-1] * n
        for i in range(n):
            for j in reversed(range(i + 1, n)):
                if height[j] >= height[i]:
                    rh[i] = j
                    break
            for j in range(i):
                if height[j] >= height[i]:
                    lh[i] = j
                    break
        '''
        ans = -1
        for i in range(n):
            if rh[i] != -1 and lh[i] != -1:
                diff = rh[i] - lh[i]
            elif rh[i] == -1 and lh[i] != -1:
                diff = i - lh[i]
            elif lh[i] == -1 and rh[i] != -1:
                diff = rh[i] - i
            elif lh[i] == rh[i] == -1:
                diff = -1
            con = diff * height[i]
            ans = max(ans, con)
        return ans
            
            
        
        