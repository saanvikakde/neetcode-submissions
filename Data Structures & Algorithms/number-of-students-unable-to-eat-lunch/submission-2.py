class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # res = len(students)
        # cnt = Counter(students)

        # for s in sandwiches:
        #     if cnt[s] > 0:
        #         res -= 1 
        #         cnt[s] -= 1 
            
        #     else: 
        #         return res 

        # return res 

        q = deque(students) 

        res = len(students) 

        for s in sandwiches: 

            count = 0 # iterations 

            while count < len(students) and s != q[0]:
                cur = q.popleft() 
                q.append(cur) # move to end of line 
                count += 1 
            
            if q[0] == s: 
                q.popleft() 
                res -= 1 
            else: 
                break
        
        return res 








         
            




        