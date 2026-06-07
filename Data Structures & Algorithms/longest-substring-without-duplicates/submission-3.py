class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = l = 0 

        seen = {} # map storing the last index of each letter 

        for r in range(len(s)): 

            if s[r] in seen: 
                l = max(seen[s[r]] + 1, l) # left pointer moves up 
            seen[s[r]] = r # update to new r 
            max_len = max(max_len, r-l+1)
            
        return max_len
            




            

        
        
            


            


        