# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # 1 find middle and end of list 

        slow, fast = head, head.next

        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 
        
        second = slow.next 
        prev = slow.next = None # splits into 2 lists 

        # 2 reverse 2nd half 
        while second: 
            tmp = second.next 
            second.next = prev 
            prev = second 
            second = tmp

        # 3 merge 2 halfs 
        first, second = head, prev # set to the new head 

        while second: 
            tmp1, tmp2 = first.next, second.next 
            first.next = second 
            second.next = tmp1 
            first = tmp1 
            second = tmp2 
        

