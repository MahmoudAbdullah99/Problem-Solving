"""
Problem Description:
    Given the head of a singly linked list, return the middle node of the linked
    list. If there are two middle nodes, return the second middle node.

Notes:
    - We need two pointers, one is slow with one step each iteration, and the
    other is fast with two steps each iteration. So when the fast reaches the
    end of the list, the slow just reaches the half of it, which is exactly
    what we want.
    - The number of the node can be odd or even, which may affect the
    termination condition of the iteration. To solve this, we need to check
    if any of the fast or the fast.next reaches Null in the while loop, then
    the slow is the result.

TODO:
    - Review.
"""

from typing import ListNode, Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
