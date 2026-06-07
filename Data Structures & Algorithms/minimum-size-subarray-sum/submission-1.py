class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        L, total = 0, 0
        min_len = len(nums)+1 
        
        for R in range(len(nums)): 
            
            total += nums[R]

            while total >= target: 
                min_len = min(R-L+1, min_len)
                total -= nums[L] # slide left out 
                L += 1 # shift the left 
           
        
        return 0 if min_len == len(nums)+1 else min_len


            
            