class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_sa = 0 

        l,r = 0,len(heights)-1

        while r > l: 
            
            max_sa = max(max_sa, min(heights[r], heights[l])*(r-l))

            if heights[r] < heights[l]: 
                r -= 1 
            else: 
                l += 1 
        
        return max_sa
            



        