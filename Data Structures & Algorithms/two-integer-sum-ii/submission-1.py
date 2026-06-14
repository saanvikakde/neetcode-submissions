class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        r = len(numbers)-1
        l = 0 
        sum = numbers[r] + numbers[l]

        while sum != target: 

            if sum > target: 
                r -= 1 

            elif sum < target: 
                l += 1 
                        
            sum = numbers[r] + numbers[l]
        
        return [l+1, r+1] 
        




