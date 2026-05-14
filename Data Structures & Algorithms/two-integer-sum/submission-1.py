class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        diff_index = {} 

        for i,n in enumerate(nums) :
            diff = target-n # the other sum in twosum is diff 
            if diff in diff_index : # if the other sum is stored 
                return [diff_index[diff], i] # return the two sums 
            diff_index[n] = i # diff_index at n (value) is set to i (counter)
        return 

        