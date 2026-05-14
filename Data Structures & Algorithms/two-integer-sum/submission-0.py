class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diff_index = {} 
        for i,n in enumerate(nums) : 
            diff = target - n 
            if diff in diff_index: 
                return [diff_index[diff], i]
            diff_index[n] = i
        return 
