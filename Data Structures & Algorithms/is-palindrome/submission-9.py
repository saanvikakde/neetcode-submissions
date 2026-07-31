class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_alnum = ''

        for c in s: 

            if c.isalnum(): 
                s_alnum += c.lower()
        
        return s_alnum == s_alnum[::-1]

    

        