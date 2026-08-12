# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        self.qSort(pairs, 0, len(pairs)-1)
        return pairs
    
    def qSort(self, pairs: List[Pair], s: int, e: int) -> None: 
        
        # base case - len <= 1 
        if e-s+1 <= 1: return 

        pivot = pairs[e] # last element 
        l = s # left pointer at 0 

        # parition so elements smaller than pivot on left side 

        for i in range(s, e): 
            if pairs[i].key < pivot.key: 
                pairs[l], pairs[i] = pairs[i], pairs[l]
                l += 1 

        # move pivot in between l and r 

        pairs[e] = pairs[l]
        pairs[l] = pivot 

        # recursion - sort left and right sides 

        self.qSort(pairs, s, l-1)
        self.qSort(pairs, l+1, e)

        