import re 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        string = re.sub(r'[^a-zA-Z0-9]', '', s)
        
        rev_index = len(string)-1 
        
        for i in range(len(string)):
            if i == rev_index : break 
            if string[i].lower() != string[rev_index].lower() : return False 
            rev_index -= 1 
        
        return True 