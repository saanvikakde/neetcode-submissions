class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s) <= 1 : return True 

        s = re.sub(r'[^a-zA-Z0-9]', '', s)

        l, r = 0, len(s)-1  

        while r > l: 

            if s[l].lower() != s[r].lower(): 
                return False 
            
            l += 1 
            r -= 1
            
        return True 
            



        