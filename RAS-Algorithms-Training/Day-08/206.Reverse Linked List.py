""""
Problem Description:
    Given the head of a singly linked list, reverse the list, and return the
    reversed list.

Notes:
    - We need three pointers, one to the previous node, one to the current
    node, and one to the next node.
    _ All we need to do is to iteratively update the next node of the current
    node to the previous node.

TODO:
    - Review.
"""

from typing import ListNode, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr

        return prev
