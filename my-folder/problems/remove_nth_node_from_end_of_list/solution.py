# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def remove(head):
            if not head:
                return 0
            
            curr = remove(head.next)
            
            if curr == n:
                head.next = head.next.next
            
            return curr + 1
        
        temp = ListNode(-1, head)
        head = temp

        remove(temp)

        return head.next
        
