# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        pre = dummy
        
        while pre.next and pre.next.next:
            later = head.next
            pre.next, later.next, head.next = later, head, later.next
            pre = head
            head = pre.next
            
        return dummy.next