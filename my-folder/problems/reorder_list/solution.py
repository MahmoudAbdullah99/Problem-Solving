# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        slow.next, slow = None, slow.next
        prev = None

        while slow:
            prev, slow.next, slow = slow, prev, slow.next
        
        asc = head

        while prev:
            asc.next, prev.next, asc, prev = prev, asc.next, asc.next, prev.next
        