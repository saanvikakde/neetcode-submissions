# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # pointer go to end - count length  
        # length - n = index of node to remove 

        cur, length = head, 0 
        
        while cur:
            length+= 1  
            cur = cur.next 
        
        index = length - n 
        if index == 0: 
            return head.next 
    
        cur = head # set back to head 
        for i in range(index): # go until prev node 

            if (i+1) == index:
                cur.next = cur.next.next # remove link 
                break 

            cur = cur.next 

        return head 

            
            




