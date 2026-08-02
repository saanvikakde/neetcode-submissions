class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l, res = 0, 0 
        seen = {} # char:index

        for i,ch in enumerate(s): 
            
            if ch in seen: 
                l = max(l,seen[ch]+1)
            seen[ch] = i 

            res = max(res, i-l+1)

        return res

            
        