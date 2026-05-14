class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_t = {}
        word_s = {} 

        if len(s) != len(t) : return False 

        for i in range(len(s)) : 
            letter_t = t[i] 
            letter_s = s[i]
            word_t[letter_t] = word_t.get(letter_t, 0) + 1 
            word_s[letter_s] = word_s.get(letter_s, 0) + 1 
        
        return word_t == word_s 