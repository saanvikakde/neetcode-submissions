class Solution:
    def hammingWeight(self, n: int) -> int:
        # find biggest power of 2 that fits 
        # go down from there, counting ones when it fits 

        ones = 0 

        print(n) 

        for i in range(32, -1, -1): 

            if n - pow(2,i) >= 0: 
                n = n - pow(2,i)
                ones += 1
        
        return ones 
        