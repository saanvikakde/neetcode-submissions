class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_sa = 0 
        l,r = 0, len(heights)-1 

        while l < r: 
            
            max_sa = max(max_sa, (min(heights[r],heights[l])*(r-l)))

            if heights[l] < heights[r]: l+=1 
            else: r-=1      
            
        return max_sa
            

            
