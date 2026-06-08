import re 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = (re.sub(r'[^a-zA-Z0-9]', '', s)).lower()
        print(s)
        
        if len(s) <= 0: return True 

        L, R = s[0], s[-1]

        for i in range(1, len(s)//2 + 1): 

            if L == R: 
                print(f"L ({L}) == R ({R})")
                L = s[i]
                R = s[-i-1]
            

            else: 
                print(f"L ({L}) != R ({R})")
                return False 
        

        return True 

