class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {} # store diff values 

        for i in range(len(nums)): 

            diff = target - nums[i]

            # does diff exist in hashmap? 

            if diff in hashmap: 
                return [hashmap[diff], i]
            
            else: 
                hashmap[nums[i]] = i


        