class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        result, temp = 0, 0 

        for n in nums: 
            if n == 1: 
                temp+= 1 
            elif n == 0: 
                result = max(result, temp)
                temp = 0 
        
        return max(result, temp) 
        