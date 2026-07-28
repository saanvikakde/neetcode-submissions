class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        return len(nums) != len(set(nums))

        # if there is a duplicate, returns true since set drops dupes 
        