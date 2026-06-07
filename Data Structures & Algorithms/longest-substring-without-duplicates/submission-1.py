class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = 0 
        L = 0 
        window = [] 

        for R in range(len(s)): 

            curr_char = s[R:R+1] 

            if curr_char in window: # if its in, remove anything from that before 
                # print(f'curr_char {curr_char} in window')
                # print(f'{index}')
            
                for i in range(window.index(curr_char) + 1): # remove anything from that before 
                    window.remove(window[0]) 
                    L += 1 
            
            window.append(curr_char) # add it to the window 

            # print(f'window: {window}, {R-L+1}')
            max_len = max(R-L+1, max_len)

        return max_len 
            




            

        
        
            


            


        