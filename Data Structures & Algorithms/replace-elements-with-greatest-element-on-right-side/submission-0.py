class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        new_arr = []

        for i in range(len(arr)-1): 

            arr.remove(arr[0])
            new_arr.append(max(arr))
        
        new_arr.append(-1)

        return new_arr
