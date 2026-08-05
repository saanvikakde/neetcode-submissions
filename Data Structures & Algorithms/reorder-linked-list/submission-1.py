# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find middle
        slow, fast = head, head.next 
        
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 

        # reverse 2nd half 
        second = slow.next
        prev = slow.next = None # end first half 

        while second: 
            tmp = second.next 
            second.next = prev 
            prev = second 
            second = tmp 

        # merge two halfs alternatively 

        first = head
        second = prev 

        while second: 
            tmp1, tmp2 = first.next, second.next 
            first.next = second 
            second.next = tmp1 
            first = tmp1 
            second = tmp2  

        
        



        