class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l = 1 

        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]: # if 2 conseq vals aren't same
                nums[l] = nums[r]
                l+=1
        return l # number unique elements

                
        