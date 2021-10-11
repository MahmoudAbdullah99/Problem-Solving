# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer_1 = head
        pointer_2 = head
        
        while pointer_1 and pointer_1.next:
            pointer_2 = pointer_2.next
            pointer_1 = pointer_1.next.next
        
        return pointer_2