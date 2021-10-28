# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head:Optional[ListNode], prev=None):
        to_comp = prev
        
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
            if head == to_comp:
                break
        
        return prev
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        
        if right <= left:
            return head

        curr = head

        while right >= 1:
            right -= 1
            curr = curr.next
        
        prev = curr
        curr = ListNode(None, head)
        
        if left == 1:
            return self.reverse(head, prev)
        
        while left > 1:
            curr = curr.next
            left -= 1
        
        curr.next = self.reverse(curr.next, prev)
        return head
