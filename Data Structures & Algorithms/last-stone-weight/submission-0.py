class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        n = len(stones)
        
        while n > 1: 
            print(f'stones {stones}')
            x = max(stones)
            stones.remove(x) 
            n -= 1
            y = max(stones) 
            stones.remove(y)

            print(f'x {x} y {y}')

            if x == y:
                print(f'n = {n}')
                n -= 1
            else: 
                print(f'appended {x-y}')
                stones.append(x-y)
                print(stones)

            
                
        if n == 1: return max(stones)
        return 0 



        