class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # kadens algorithim - sliding window 

        currSum = 0 
        maxSum = nums[0]

        for i in range(len(nums)): # i goes from 0..end of nums
                        
            if currSum < 0: # largest sum shouldn't be less than zero 
                print(f"current sum is below zero. {currSum}")
                currSum = 0 
            
            currSum += nums[i]
            print(f'new sum: {currSum}')
        
            maxSum = max(currSum, maxSum)
        
        return maxSum
