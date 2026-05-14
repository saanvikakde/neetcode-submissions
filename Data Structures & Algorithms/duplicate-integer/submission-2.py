class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        values = list() 

        for n in nums: 
            if n in values : return True
            values.append(n) 


        return False