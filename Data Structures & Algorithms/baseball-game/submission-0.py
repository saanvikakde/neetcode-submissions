class Solution:
    def calPoints(self, operations: List[str]) -> int:

        res = [] 

        for i in range(len(operations)): 

            if operations[i] == '+': 
                res.append(int(res[-1]) + int(res[-2]))

            elif operations[i] == 'D': 
                res.append(int(res[-1])*2)

            elif operations[i] == 'C': 
                res.remove(res[-1])
            
            else: res.append(int(operations[i]))
        
        return sum(res)
        


        
         
        