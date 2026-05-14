class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurences = dict() 

        for n in nums : 
            occurences[n] = occurences.get(n,0) + 1 
            if occurences[n] > 1 : return True 

        return False 

    