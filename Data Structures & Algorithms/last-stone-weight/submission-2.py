class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        n = len(stones)
        
        while n > 1: 
            x = max(stones)
            stones.remove(x) 
            n -= 1
            y = max(stones) 
            stones.remove(y)


            if x == y:
                n -= 1
            else: 
                stones.append(x-y)

            
                
        if n == 1: return stones[0]
        return 0 



        