class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        counter =0
        result=0

        for num in nums:
            if num:
                counter = counter +1
            else:
                counter =0;
            result = max(result, counter)
        return result
                
            
           
            
            

        
                

        