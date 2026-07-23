class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = [] 

        parens = {')' : '(',']' : '[','}' : '{'}

        if s[0] in parens: return False # if we start with closing 

        for c in s: 
            if c in parens: # if closing 
                if stack and stack[-1] == parens[c]: 
                    stack.pop() 
                else: return False 
            
            else: 
                stack.append(c) # opening 
         
            
        return not stack 

        