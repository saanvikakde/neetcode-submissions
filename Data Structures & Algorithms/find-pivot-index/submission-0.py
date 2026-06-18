class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        prefix = [] 
        total = 0 
        prefix.append(0)

        for n in nums: 
            total += n 
            prefix.append(total)
            
        for i in range(len(nums)): 
            left_sum = prefix[i]
            right_sum = prefix[len(nums)] - prefix[i+1]

            if left_sum == right_sum: return i 
        
        return -1 




        
        