class Solution:
    def trap(self, h: List[int]) -> int:
        max_left = h[0]
        max_right = h[-1]
        l, r = 0, len(h) - 1
        res = 0
        
        while l < r:
            if max_left <= max_right:
                l += 1
                max_left = max(max_left, h[l])
                res += max_left - h[l]
            else: 
                r -= 1
                max_right = max(max_right, h[r])
                res += max_right - h[r]
                
        return res
        
        
   
            
            
            