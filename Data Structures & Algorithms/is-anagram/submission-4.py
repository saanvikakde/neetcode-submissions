class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t) : return False 

        s_letteroccur = dict() 
        t_letteroccur = dict() 

        for c in s: 
            s_letteroccur[c] = s_letteroccur.get(c,0) + 1 

        for c in t: 
            t_letteroccur[c] = t_letteroccur.get(c,0) + 1 

        print(s_letteroccur)
        print(t_letteroccur)

        if s_letteroccur == t_letteroccur : return True 

        return False