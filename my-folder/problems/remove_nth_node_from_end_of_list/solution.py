# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def remove(head, n):
            if head == None:
                return head, 0
            
            head.next, counter = remove(head.next, n)
            counter += 1

            if counter == n:
                head = head.next
            
            return head, counter
        
        return remove(head, n)[0]