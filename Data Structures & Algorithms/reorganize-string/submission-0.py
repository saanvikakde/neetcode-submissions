class Solution:
    def reorganizeString(self, s: str) -> str:
        
        freq = Counter(s) 

        heap = [ [-c, char] for char,c in freq.items() ]
        heapq.heapify(heap)

        prev, res = None, "" 

        while heap or prev: 

            if prev and not heap: return "" # no char for in-between 

            count, char = heapq.heappop(heap) # gives max freq char 
            res += char 
            count += 1 

            if prev: # add val back 
                heapq.heappush(heap, prev)
                prev = None 
            
            if count != 0: # will need to add it back 
                prev = [count, char]
        
        return res 
            



            
        