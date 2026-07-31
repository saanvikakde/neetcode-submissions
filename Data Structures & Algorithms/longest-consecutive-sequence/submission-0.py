class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = sorted(set(nums)) 
        
        if nums == [] : return 0 
        
        r = 0 
        ans = 1 

        for l in range(1, len(nums)): 

            print(f'r, l {nums[r + (l-r-1)]} {nums[l]}')
            
            # compare left window to next value in right window 
            if nums[l] != nums[r  + (l-r-1)] + 1: 
                r = l # move right pointer 
            
            ans = max(ans, l-r+1)
        
        return ans


        