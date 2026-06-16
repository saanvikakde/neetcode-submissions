class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_sa = 0 

        for l in range(len(heights)): 

            for r in range(l+1, len(heights)): 
                
                sa = min(heights[l], heights[r])*(r-l)
                max_sa = max(sa,max_sa)
            
        return max_sa




        