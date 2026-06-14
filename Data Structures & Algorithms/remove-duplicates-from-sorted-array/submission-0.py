class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l,r = 0,1

        while r < len(nums): 

            print(f'{nums} {l}: {nums[l]} {r}: {nums[r]}')

            if nums[l] == nums[r]: 
                print(f'removing {nums[r]}')
                nums.remove(nums[r])

            
            elif nums[l] != nums[r]: 
                r+= 1
                l = r-1

        return len(nums) 
                
        