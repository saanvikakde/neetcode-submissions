class Solution:
    def string_to_dict(s: str) -> dict(): 
        answer = dict() 
        for letter in s: 
            answer[letter] = answer.get(letter, 0) + 1 
            
        return answer 

    def isAnagram(self, s: str, t: str) -> bool:
        
        word_s = Solution.string_to_dict(s) 
        word_t = Solution.string_to_dict(t) 

        print(word_s)
        print(word_t)


        if word_s == word_t : return True 

        return False 

  
        