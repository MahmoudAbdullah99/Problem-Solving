# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            curr = head
            head = head.next
            curr.next = prev
            prev = curr

        if fast:
            head = head.next

        while head:
            if prev.val != head.val:
                return False
            head = head.next
            prev = prev.next

        return not prev