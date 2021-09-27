""""
Problem Description:
    Given the head of a linked list and an integer val, remove all the nodes of
    the linked list that has Node.val == val, and return the new head.

Notes:
    - There are some edge-cases we need to take care of:
        - The linked list is empty, i.e. the head node is None.
        - The head node has the target value.
        - Multiple nodes with the target value in a row.
        - The last node has the target value.
    - In order to save the "head" as special, twe need a "dummy" head. This
    will help in the case of needing to remove the head and there are some of
    the nodes after it.

TODO:
    - Review.
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements_1(self, head: Optional[ListNode], val: int) -> \
            Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            if not prev and curr.val == val:
                head = head.next
                curr = head
                continue
            elif prev and curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return head

    def removeElements_2(self, head: Optional[ListNode], val: int) -> \
            Optional[ListNode]:
        prev = ListNode(-1)
        prev.next = head
        curr = prev

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return prev.next
