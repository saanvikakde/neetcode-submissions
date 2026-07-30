class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {} # difference : index

        for i in range(len(nums)): 
            
            diff = target - nums[i]

            print(f'{nums[i]} - {target} = {diff}')
            
            if diff in hashmap: # see if that key we need exists 
                return [hashmap[diff], i]

            else: 
                hashmap[nums[i]] = i 


        

            


        