class Solution:

    def encode(self, strs: List[str]) -> str:

        # encode list of strings into a string 
        # have some combination/hash value in bteween each string  


        hashval = 'thisisthehashval'
        res = ''

        for i in range(len(strs)):

            res = res + hashval + strs[i]
        
        return res 

    def decode(self, s: str) -> List[str]:

        # decode string back into the list of strings 

        if len(s) <= 0: return [] 

        hashval = 'thisisthehashval'

        return s.split(hashval)[1:]
