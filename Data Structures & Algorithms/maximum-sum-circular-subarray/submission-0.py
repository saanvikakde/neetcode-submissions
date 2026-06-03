class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        currSum = 0 
        maxSum = nums[0]
        n = len(nums)

        for i in range(n): # repeat n times (left pointer)
            currSum = 0 
            for j in range(i,i+n): # shifting right pointer
                currSum += nums[j % n]
                maxSum = max(currSum, maxSum)
        
        return maxSum 
        





