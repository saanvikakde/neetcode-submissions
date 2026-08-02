class Solution:
    def trap(self, height: List[int]) -> int:

        if not height: return 0 
        
        l, r = 0, len(height)-1
        curr, total = 0,0
        max_r, max_l = height[r],height[l]  

        while l < r: 
            if max_l < max_r:
                l += 1 
                max_l = max(max_l, height[l])
                total += max_l - height[l]
            else: 
                r -=1 
                max_r = max(max_r, height[r])
                total += max_r - height[r]
        
        return total

            

            




            



            

        
        