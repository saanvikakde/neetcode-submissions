class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        maxx = 0;

        for i in range(len(nums)):
            counter =0
            for j in range(i, len(nums)):
                if(nums[j] != 0):
                    counter+=1;
                else:
                    break;
            maxx = max(maxx, counter)

        return maxx

            
                

        