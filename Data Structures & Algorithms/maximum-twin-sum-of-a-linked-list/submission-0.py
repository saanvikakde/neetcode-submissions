# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow = fast = head 
        prev = None

        while fast and fast.next: # reverse first half  
            fast = fast.next.next 
            tmp = slow.next 
            slow.next = prev # reverse link 
            prev = slow 
            slow = tmp 
        
        max_sum = 0 
        
        while slow: # prev points to reversed first half, slow to second half 
            max_sum = max(max_sum, prev.val + slow.val)
            prev = prev.next 
            slow = slow.next

        return max_sum 
        
        
        
            
            
        
        





        