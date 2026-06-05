class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        # sliding window approach, keeps 2 values the same (FIFO)
        n = len(arr) 
        res, window_sum = 0, 0

        for i in range(n):
        
            window_sum += arr[i] # entire window added

            if i >= k-1: # window is filled 
            
                if (window_sum/k) >= threshold: 
                    res+=1
                
                window_sum -= arr[i-k+1] # remove element that just left window 
                
        return res


        