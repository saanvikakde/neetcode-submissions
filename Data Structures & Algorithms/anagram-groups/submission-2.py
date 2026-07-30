class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # create a hashmap with 
        # key: letter freq (tuple) value: associates strings (list) 

        res = defaultdict(list) 

        for s in strs: 

            count = [0] * 26 

            for c in s: 

                count[ord(c) - ord('a')] += 1 
            
            res[tuple(count)].append(s) 
        
        return list(res.values())

        


        




        