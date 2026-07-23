class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = [] 

        parens = {')' : '(',']' : '[','}' : '{'}

        for c in s: 
            if c in parens: # if closing 
                if stack and stack[-1] == parens[c]: 
                    stack.pop() 
                else: return False 
            
            else: 
                stack.append(c) # opening 
         
            
        if stack: return False 

        return True 

        