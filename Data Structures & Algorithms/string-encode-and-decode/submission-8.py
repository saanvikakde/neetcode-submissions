class Solution:

    def encode(self, strs: List[str]) -> str:

        # encode list of strings into a string 
        # have some combination/hash value in bteween each string 
        # include the length of the word incase hash value is the string


        res = ''

        for word in strs: 
            res += str(len(word)) + '#'+ word 
        return res 

    def decode(self, s: str) -> List[str]:

        # decode string back into the list of strings 

        res = [] 

        i = 0 

        while i < len(s): 
            word = ''
            index = s.find('#',i) # starting from i 
            length = int(s[i:index])
            word += s[index+1:index+1+length]
            res.append(word)
            i = index + length + 1 
        
        return res 

