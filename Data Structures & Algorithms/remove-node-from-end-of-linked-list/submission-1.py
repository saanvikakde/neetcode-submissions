# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        cur = head
        length = 0 
        
        while cur:
            length += 1 
            cur = cur.next 
        
        index = length - n 

        cur = head 
                
        for i in range(index): 
            
            if (i+1) == index: 
                cur.next = cur.next.next 
                break 
            
            cur = cur.next 
        
        if index == 0: return head.next 
        return head


            
